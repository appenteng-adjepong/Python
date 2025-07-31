import pandas as pd
import csv
from datetime import datetime as dt
from data_entry import *

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"

    @classmethod
    def intialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df  = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)
            
    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
    
        with open(cls.CSV_FILE, "a", newline="") as csvfile: # known as a context manager
        # automatically handles closing files and memory leaks
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS) 
            writer.writerow(new_entry)
        print('Entry added successfully')

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        start_date = dt.strptime(start_date, CSV.FORMAT)
        end_date = dt.strptime(end_date, CSV.FORMAT)

        mask = (df["date"] >= start_date & (df["date"] <= end_date))
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No transactions found in the given date range")
        else:
            print(f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}))

            total_income = filtered_df["category"] == ["Income"]["amount"].sum()
            total_expense = filtered_df["category"] == ["Expense"]["amount"].sum()
            print("\nSummary: ")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Savings: ${(total_income - total_expense):.2f}")
        return filtered_df
            
            
        
    def add():
        CSV.intialize_csv()
        date = get_date("Enter the date of the transaction (dd-mm-yyyy) or presss enter for today's date", allow_default=True)
        amount = get_amount()
        category = get_category()
        description = get_description()
        CSV.add_entry(date, amount, category, description)

CSV.get_transactions("01-01-2023", "08-10-2024")



