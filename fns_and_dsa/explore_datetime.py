from datetime import datetime, timedelta

def display_current_datetime():
    # save the current date and time
    current_date = datetime.now()
    
    # format and print
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")


def calculate_future_date():
    # ask user for number of days
    days = int(input("Enter the number of days to add to the current date: "))

    # save the future date
    future_date = datetime.now() + timedelta(days=days)

    # format and print
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")


if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()