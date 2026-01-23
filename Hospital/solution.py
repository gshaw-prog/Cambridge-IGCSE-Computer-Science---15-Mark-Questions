# Constants for the acceptable temperature range
MIN_TEMP = 36.0
MAX_TEMP = 37.5

# Arrays and variables to store data for Task 2 and 3
temperatures = []
out_of_range_count = 0

print("--- Hospital Cot Monitoring System ---")

# TASK 1 & 2: Data entry for a 3-hour period (18 readings total)
# 3 hours = 180 minutes. Recorded every 10 minutes = 18 readings.
for i in range(18):
    valid_input = False
    
    while not valid_input:
        try:
            # Task 1: Prompt for entry and validate data type
            temp = float(input(f"Enter reading {i+1} temp (°C): "))
            valid_input = True
            
            # Task 1: Check range and output suitable messages
            if temp < MIN_TEMP:
                print(">> Warning: Temperature is too low.")
                out_of_range_count += 1
            elif temp > MAX_TEMP:
                print(">> Warning: Temperature is too high.")
                out_of_range_count += 1
            else:
                print(">> Temperature is within acceptable range.")
                
            # Task 2: Store temperature in an array
            temperatures.append(temp)
            
        except ValueError:
            print("Invalid input. Please enter a numerical value (e.g., 36.5).")

# TASK 2: Calculate Highest, Lowest, and Difference
highest_temp = temperatures[0]
lowest_temp = temperatures[0]

for t in temperatures:
    if t > highest_temp:
        highest_temp = t
    if t < lowest_temp:
        lowest_temp = t

temp_diff = highest_temp - lowest_temp

# Task 2 Outputs
print("\n--- 3-Hour Summary ---")
print(f"Highest Temperature: {highest_temp}°C")
print(f"Lowest Temperature:  {lowest_temp}°C")
print(f"Temperature Difference: {temp_diff:.1f}°C")

# TASK 3: Check for alerts and output summary
# Conditions: Difference > 1.0 OR out of range more than twice
if temp_diff > 1.0 or out_of_range_count > 2:
    print("\n*** ALERT: MEDICAL ATTENTION REQUIRED ***")
    print("Summary of Problems:")
    if temp_diff > 1.0:
        print(f"- Large temp fluctuation detected ({temp_diff:.1f}°C).")
    if out_of_range_count > 2:
        print(f"- Baby was out of safe range {out_of_range_count} times.")
else:
    print("\nStatus: Monitoring stable. No immediate action required.")

# Task 1 (Data Entry & Validation): * The program allows entry of temperatures.
# It uses selection (if/elif/else) to check if the temperature is too high, too low, or acceptable and provides specific messages.
#Validation is enforced using a while loop to ensure a value is entered correctly.

# Task 2 (Storage & Statistics):
# The program stores 18 readings (3 hours at 10-minute intervals) in a list.
# It uses a loop to find the maximum and minimum values rather than just built-in functions, demonstrating exam-level logic.
# It calculates the difference between the high and low.

# Task 3 (Alert Summary):
#It uses a compound if statement with an or operator to check if the temperature difference exceeds 1.0 or if the range was exceeded more than twice.
#A summary message is printed only if these specific conditions are met.

#Program Quality:
#Meaningful variable names like out_of_range_count and temp_diff are used throughout.