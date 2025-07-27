import datetime
from datetime import timedelta

def display_current_datetime():
  current_datetime = datetime.datetime.now()
  print(f"Current date and time: {current_datetime.strftime("%Y-%m-%d %H:%M:%S")} ")

def calculate_future_date():
    day = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.datetime.now()
    delta = datetime.timedelta(days = day)
    future_date = current_date.date() + delta
    print(f"Future date: {future_date.strftime("%Y-%m-%d")} ")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
