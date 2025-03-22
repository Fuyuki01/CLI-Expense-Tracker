import json
import os
import argparse
import datetime, calendar

expanses_list = "expanses.json"

def list_all_expenses():
    try:
        with open(expanses_list, 'r') as file:
            expanses = json.load(file)
        return expanses
    except FileNotFoundError:
        return []


def summary(month=12):
    expanses = list_all_expenses()
    sum = 0
    for expanse in expanses:
        date_obj = datetime.datetime.strptime(expanse['date'], "%d-%m-%Y")
        month_time = date_obj.month
        if month == 12 or month_time == month:
            sum += int(expanse['amount'])
    if month != 12:
        month_name = calendar.month_name[month]
        print(f"Total expenses for {month_name}: ${sum}")
    else:
        print(f"Total expenses for all months: ${sum}")


def add_expanse(description, amount):
    try:
        expanses = list_all_expenses()
        now = datetime.datetime.now().strftime("%d-%m-%Y")

        new_expanse = {
            "id": len(expanses) + 1,
            "date": now,
            "description": description,
            "amount": int(amount)
        }
        expanses.append(new_expanse)

        with open(expanses_list, "w") as file:
            json.dump(expanses, file, indent=4)

        print(f"Expense added: {new_expanse['description']} - ${new_expanse['amount']}")

    except Exception as e:
        print(f"Error adding expense: {e}")


def delete_expanse(id):
    try:
        expanses = list_all_expenses()
        removed = False

        for expanse in expanses:
            if  expanse['id'] == int(id):
                expanses.remove(expanse)
                print(f"Expense deleted successfully {id}")
                removed = True
        
        if removed:
            for index, expanse in enumerate(expanses, start=1):
                expanse['id'] = index

            with open(expanses_list, "w") as file:
                json.dump(expanses, file, indent=4)

    except Exception as e:
        print(f"Error removing expanse: {e}")


def main():
    while True:
        command = input("$ ").strip().split(" ", 1)

        if not command:
            continue
        
        action = command[0]

        if action == "list":
            expanses = list_all_expenses()
            print(f"{'ID':<4} {'Date':<12} {'Description':<25} {'Amount':>6}")
            print("-" * 60)
            for expanse in expanses:
                print(f"{expanse['id']:<4} {expanse['date']:<12} {expanse['description']:<25} ${expanse['amount']:>4}")
        elif action == "summary":
            if len(command) > 1:
                parse = argparse.ArgumentParser(prog="summary", add_help=False)
                parse.add_argument("--month", type=int, help="month to calculate the summary")
                try:
                    args = parse.parse_args(command[1].split())
                    summary(args.month)
                except Exception as e:
                    print("Usage: summary --month 5")
                    print("Error:", e)
            else:
                print(f"${summary()}")
        elif action == "add":
            add_parser = argparse.ArgumentParser(prog="add",add_help=False)
            add_parser.add_argument("--description", required=True, help="Description of the expanse")
            add_parser.add_argument("--amount", type= int, required=True, help="Amount of the expanse")
            try:
                args = add_parser.parse_args(command[1].split())
                add_expanse(args.description, args.amount)
            except:
                print("Usage: add --description \"Lunch\" --amount 20")
        elif action == "remove":
            parser = argparse.ArgumentParser(prog="remove", add_help=False)
            parser.add_argument("--id", type=int, required=True, help="ID of the expanse")
            try:
                args = parser.parse_args(command[1].split())
                delete_expanse(args.id)
            except:
                print("Usage: remove --id 2")
        elif action in ["clear", "leave", "quit"]:
            break


if __name__ == "__main__":
    main()
