import json
import datetime

def create_date_day_json(start_date_str, end_year, output_filename="date_day_output.json"):
    """
    Creates a JSON file with dates as keys and days of the week as values,
    from a start date to the end of a given year.

    Args:
        start_date_str (str): Start date in 'YYYY-MM-DD' format (e.g., '1582-10-15').
        end_year (int): The year to end the date range (inclusive).
        output_filename (str): The name of the JSON file to create.
    """
    try:
        start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError("Invalid start_date_str format. Please use 'YYYY-MM-DD'.")

    end_date = datetime.date(end_year, 12, 31)
    date_day_dict = {}
    current_date = start_date

    while current_date <= end_date:
        day_of_week = current_date.strftime('%A') # Full day name (e.g., Monday)
        date_key = current_date.strftime('%Y-%m-%d') # Format date as YYYY-MM-DD
        date_day_dict[date_key] = day_of_week
        current_date += datetime.timedelta(days=1)

    with open(output_filename, 'w') as json_file:
        json.dump(date_day_dict, json_file, indent=4) # indent for pretty formatting

    print(f"JSON file '{output_filename}' created successfully.")

if __name__ == "__main__":
    start_date = "1582-10-15"
    end_year = 3000
    output_file = "date_day.json"

    create_date_day_json(start_date, end_year, output_file)
