__package__

def is_leap_year(year):
    """
    Check if a given year is a leap year.

    Parameters:
    - year (int): The year to be checked.

    Returns:
    - bool: True if the year is a leap year, False otherwise.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days_in_month(year, month):
    """
    Get the number of days in a specific month of a given year.

    Parameters:
    - year (int): The year.
    - month (int): The month (1 to 12).

    Returns:
    - int: The number of days in the specified month of the given year.
    """
    days_in_month = [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_in_month[month - 1]

def input_birth():
    try:
        # Get year
        year = int(input('\nPlease input the year of your birth (1901-2050):\n '))
        if year < 1901 or year > 2050:
            raise ValueError("\nYear must be between 1901 and 2050.")

        # Get month
        month = int(input('\nPlease input the month of your birth (1-12): \n'))
        if month < 1 or month > 12:
            raise ValueError("\nMonth must be between 1 and 12.")

        # Get day
        day = int(input(f'\nPlease input the day of your birth (1-{get_days_in_month(year, month)}): \n'))
        if day < 1 or day > get_days_in_month(year, month):
            raise ValueError(f"\nDay must be between 1 and {get_days_in_month(year, month)}.")

        # Get hour
        hour = int(input('\nPlease input the hour of your birth (please use 24-hour system by inputing an integer between 0 and 23):\n '))
        if hour < 0 or hour > 23:
            raise ValueError("\nHour must be between 0 and 23.")
        
        sex = input('\nPlease input your BIOLOGICAL gender by inputting "Female" or "Male" (we totally respect different gender identities especially those non-binary ones and decry any form of gender discrimination):\n')
        if sex not in ["Male","Female"]:
            raise ValueError("\nPlease check the Capitalization of your Input and ensure no space in your input:\n")
        
        print(f"\nUser input: {[year, month, day, hour]} and {sex}\n")
        
        return [year, month, day, hour],sex

    except ValueError as e:
        print(f"\nInvalid input: {e}")
        print("\nInput validation failed. Exiting. Please Re-Launch me.\n")
       
        return e
    


