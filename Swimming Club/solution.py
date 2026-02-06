# Initialize data structures and variables
names = []
times = []
total = 0.0
fastest_time = 101.0  # Must be higher than any possible valid entry
winner_name = ""

# Loop for 50 swimmers
for i in range(50):
    name_input = input(f"Enter name for swimmer {i+1}: ")
    names.append(name_input)
    
    # Input and Validation
    time_input = float(input(f"Enter race time for {name_input}: "))
    while time_input < 20.0 or time_input > 100.0:
        print("Invalid entry. Time must be between 20.0 and 100.0.")
        time_input = float(input("Please re-enter time: "))
    
    times.append(time_input)
    
    # Update running total
    total += time_input
    
    # Find the winner (minimum value logic)
    if time_input < fastest_time:
        fastest_time = time_input
        winner_name = name_input

# Final calculations and display
average_time = total / 50

print("\n--- Race Results ---")
print(f"Club Average Time: {average_time:.2f} seconds")
print(f"Competition Winner: {winner_name} ({fastest_time} seconds)")
