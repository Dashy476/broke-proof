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