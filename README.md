# CLI Expense Tracker

A simple interactive command-line tool to **add, delete, and summarize personal expenses** stored in a **JSON file**

---

## Features

- Add new expenses with description and amount  
- Delete expenses by ID  
- List all recorded expenses  
- View total or monthly expense summaries 

---

## Clone the Repository

```bash
git clone https://github.com/Fuyuki01/CLI-Expense-Tracker.git
cd CLI-Expense-Tracker
```

---

## Running the Program

Once inside the project folder, run:

```
python main.py
```

---

## Usage

### Adding an Expense

```
add --description "Lunch" --amount 15
```

**Output:**
```
Expense added: Lunch - $15
```

---

### Listing All Expenses

```
list
```

**Output:**
```
ID   Date         Description               Amount
-----------------------------------------------------
1    22-03-2025   Lunch                     $  15
2    22-03-2025   Coffee                    $   5
```

---

### Deleting an Expense

```
remove --id 1
```

**Output:**
```
Expense deleted successfully 1
```

---

### Viewing a Monthly Summary

```
summary --month 3
```

**Output:**
```
Total expenses for March: $45
```

Or to view the total for **all months**:

```
summary
```

---

### Exiting the CLI

```
quit
clear
leave
```

---

## Project URL
https://roadmap.sh/projects/expense-tracker
