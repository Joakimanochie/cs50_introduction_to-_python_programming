def convert(time_str):
    # Split the time string into hours and minutes
    hours, minutes = map(int, time_str.split(':'))
    # Calculate the corresponding number of hours as a float
    return hours + minutes / 60

def main():
    # Prompt the user for a time in 24-hour format
    time_input = input("Enter the time (HH:MM): ")

    # Use the convert function to get the time in hours as a float
    time_in_hours = convert(time_input)

    # Define the meal time ranges
    breakfast_start = 7.0
    breakfast_end = 8.0
    lunch_start = 12.0
    lunch_end = 13.0
    dinner_start = 18.0
    dinner_end = 19.0

    # Check if the input time falls within any of the meal time ranges
    if breakfast_start <= time_in_hours <= breakfast_end:
        print("It's breakfast time!")
    elif lunch_start <= time_in_hours <= lunch_end:
        print("It's lunch time!")
    elif dinner_start <= time_in_hours <= dinner_end:
        print("It's dinner time!")

if __name__ == "__main__":
    main()
