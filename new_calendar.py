import calendar

#ask the user for input
year = int(input("Eneter the year e.g(2025): "))
month = input("Enter the month (1-12 or 'all' for full year): ")

if month.lower() == "all":
    # Print full year calendar
    print("\n", calendar.TextCalendar().formatyear(year))
else:
    month = int(month)
    # Print calendar for a single month
    print("\n", calendar.month(year, month))
