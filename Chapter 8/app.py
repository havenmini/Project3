from nepali_datetime import date as nepali_date
from datetime import datetime, timedelta

def calculate_age_nepali(birth_date_nepali):
    # Convert Nepali date to Gregorian date
    birth_date_gregorian = birth_date_nepali.to_datetime_date()
    today = datetime.today()
    
    # Calculate age in years, months, and days
    years = today.year - birth_date_gregorian.year
    months = today.month - birth_date_gregorian.month
    days = today.day - birth_date_gregorian.day
    
    # Adjust for negative values
    if days < 0:
        months -= 1
        days += (birth_date_gregorian.replace(year=today.year, month=today.month) - birth_date_gregorian.replace(year=today.year, month=today.month - 1)).days
    
    if months < 0:
        years -= 1
        months += 12
    
    return years, months, days

# Example usage
nepali_year = int(input("Enter Nepali birth year (YYYY): "))
nepali_month = int(input("Enter Nepali birth month (MM): "))
nepali_day = int(input("Enter Nepali birth day (DD): "))

birth_date_nepali = nepali_date(nepali_year, nepali_month, nepali_day)
years, months, days = calculate_age_nepali(birth_date_nepali)
print(f"You are {years} years, {months} months, and {days} days old.")
