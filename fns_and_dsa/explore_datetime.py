from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now() 
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print (f'Current date and time is: {formatted_date}') 
days_to_add = int(input('Enter the number of days to add to the current date: '))

def calculate_future_date():
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print( f'Future date:{formatted_future_date}')

def main():
    # Display the current date and time
    display_current_datetime()
    
    # Calculate and display the future date
    calculate_future_date()

# Entry point of the script
if __name__ == "__main__":
    main()

