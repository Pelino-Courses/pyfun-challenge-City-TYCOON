from datetime import datetime

# Define parameters of our function
def date_calculator(start_date, end_date):
    """Welcome, you have to enter dates in YYYY-MM-DD format."""
    # Calculate the time difference in days and handle errors
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        difference = abs((end_date - start_date).days)
        return difference
    except ValueError:
        return "Error: Dates must be in YYYY-MM-DD format."

# Print the function's docstring
print(date_calculator.__doc__)

# Get user input for start and end dates
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")

# Call the function and print the result
result = date_calculator(start_date, end_date)
print(f"Difference in days: {result}" if isinstance(result, int) else result)