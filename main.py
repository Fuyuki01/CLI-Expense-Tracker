import json
import os
import sys
import datetime, calendar
import MainWindow

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
    app = MainWindow.QApplication(sys.argv)

    window = MainWindow.MainWindow()

    window.show()
    app.exec()


if __name__ == "__main__":
    main()
