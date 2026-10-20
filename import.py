import csv
import sqlite3
import pathlib
import datetime
import calendar


class Transaction:

    def __init__(self, account, date, description, amount):
        self.account = account
        self.date = date
        self.description = description
        self.amount = amount

    def __repr__(self):
        return (f"Transaction(account={self.account}, date={self.date}, "f"description={self.description}, amount={self.amount:.2f})")

    def transfer(self):
        return "TRANSFER" in self.description.upper()


class Bill:

    def __init__(self, name, amount, due_day, keyword):
        self.name = name
        self.amount = amount
        self.due_day = due_day
        self.keyword = keyword

    def days_until_due(self):
        today = datetime.date.today()
        year, month = today.year, today.month
        if today.day > self.due_day:
            month += 1
            if month == 13:
                month, year = 1, year + 1
        last_day = calendar.monthrange(year, month)[1]
        due = datetime.date(year, month, min(self.due_day, last_day))
        return (due - today).days

    def __repr__(self):
        return f"Bill(name={self.name}, amount={self.amount:.2f}, due_day={self.due_day})"


class Income:

    def __init__(self, source, rate, keyword):
        self.source = source
        self.rate = rate
        self.keyword = keyword

    def __repr__(self):
        return f"Income(source={self.source}, rate={self.rate:.2f})"


def main():

    path = pathlib.Path(r"D:/Python/broke-proof/data")

    DB = sqlite3.connect("transactions.db")
    cursor = DB.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS transactions " "(account TEXT, date TEXT, description TEXT, amount REAL)")

    for file in path.glob("*.csv"):
        with open(file, "r", newline="") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                account = row[0]
                date = datetime.date.fromisoformat(row[1])
                description = row[2]
                amount = float(row[5])
                if row[4] == "Debit":
                    amount = -amount

                transaction = Transaction(account, date, description, amount)
                cursor.execute(
                    "INSERT INTO transactions VALUES (?, ?, ?, ?)",
                    (account, date.isoformat(), description, amount),
                )
                print(transaction)

    DB.commit()
    DB.close()


if __name__ == "__main__":
    main()