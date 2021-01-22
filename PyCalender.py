# Import the calender module.
import calendar

# Get the year and month.
print('Please enter the year(in number): ')
Year = int(input())
print('Please enter the month(in number): ')
Month = int(input())

# Function to print the calender.
def Print_Calender(Year, Month):
    print('\nHeres the calender for this month: ')
    print(calendar.month(Year, Month))
    return

# Call the Print_Calender function.
Print_Calender(Year, Month)

# Wait for user input before exitting.
input('\nPress enter to exit')