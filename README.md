# Broke-Proof

A command-line budget tool that turns my bank exports into a clear picture of where my money goes and how close I am to a $1,000 savings cushion.

## The problem
I'm a full-time student working flexible hours. My bills, like car insurance and a loan payment, hit on different dates, and my spending is spread across groceries, gas, and food. I couldn't easily answer "How much did I spend this week?" or "How many more work hours do I need to reach my goal?"

## What it does
- Imports checking and savings CSV exports into a local SQLite database
- Skips transfers between my own accounts so nothing gets counted twice
- Sorts transactions into categories based on merchant names
- Tracks recurring bills and their due dates
- Reports weekly spending, upcoming bills, and progress toward the savings goal, including the work hours needed to hit it by a target date

## Tech
Python 3, SQLite, `csv`, `sqlite3`

## Security and privacy
Real financial data never goes into this repo. CSVs and the database are listed in `.gitignore`, and any sample data is fake. See `SECURITY.md` for the threat model.

## Roadmap
- [ ] Level 1: CSV import, categorizing, bill tracking, cushion report
- [ ] Level 2: Encrypted database, dashboard, bill reminders, income forecast
- [ ] Level 3: Security testing of the app itself, with a written report

## Status
In progress, started October 2026.

## Design Notebook: Level 1, `import.py`

### Problem Statement
I don't know where my money goes, since my spending is buried in messy bank statements. I need my transactions in one place and tracked. That takes an import tool that reads each bank export and stores it in a database.

### Understandings
- I understand file paths: pointing the program to a folder and the files inside it.
- I need to brush up on object-oriented programming, since it's key to organizing the data cleanly.
- My SQL knowledge is basic and needs more research.

### Design Sketch
```
checking.csv   savings.csv
       \           /
     read each row
  (account, date, description, credit/debit, amount)
            |
     Transaction object
  (signed amount, transfer check)
            |
      SQLite database

Bill and Income are separate classes. Transactions get
matched to them later; they aren't created during import.
```

### Pseudocode
```
for each CSV file in the data folder:
    skip the header row
    for each row:
        read account, date, description
        make the amount negative if it's a debit
        create a Transaction
        insert it into the database
save (commit) and close the database
```

### Lessons Learned
- Look at the real data first. The dates are text, not numbers, and the descriptions are all uppercase.
- The amount is the most important field, and its sign comes from the Credit/Debit column.
- Inheritance means "is a." A bill isn't a transaction; it's something a transaction pays. Separating them simplified the code.
- Not every withdrawal is a bill. Sorting belongs after the import, not during it.
- SQLite inserts don't save until `commit()`.
- Methods should return clear values (`False`, not `None`).
- **Still to do:** prevent duplicate imports and remove the hardcoded file path.