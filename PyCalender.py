# Import the calendar module.
import calendar

# Get the year and month.
print('Please enter the year(in number): ')
Year = int(input())
print('Please enter the month(in number): ')
Month = int(input())

# Function to print the calendar.
def Print_Calendar(Year, Month):
    print('\nHeres the calendar for this month: ')
    print(calendar.month(Year, Month))
    return

# Call the Print_Calendar function.
Print_Calendar(Year, Month)

# Wait for user input before exitting.
input('\nPress enter to exit')