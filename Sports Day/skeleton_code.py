# --- INITIALIZATION ---
# HouseNames is a 1D array (List)
house_names = ["Red", "Blue", "Green", "Yellow"]

# ScoreTable is a 2D array (List of Lists) 
# Initializing 4 rows and 5 columns with 0
score_table = [[0 for j in range(5)] for i in range(4)]

# TotalPoints is a 1D array to store the sum for each house
total_points = [0, 0, 0, 0]

# --- TASK 2: INPUT & VALIDATION ---
for house_index in range(4):
    print(f"Entering scores for House: {house_names[house_index]}")
    for event_index in range(5):
        valid = False
        while not valid:
            score = int(input(f"  Enter score for Event {event_index + 1}: "))
            # FIXME: Add a range check here (score must be between 0 and 10)
            if score >= 0 and score <= 10:
                score_table[house_index][event_index] = score
                valid = True
            else:
                print("Invalid input. Score must be between 0 and 10.")

# --- TASK 3: CALCULATION ---
for house_index in range(4):
    house_total = 0
    for event_index in range(5):
        # FIXME: Add the score from score_table to house_total
        house_total = house_total + score_table[house_index][event_index]
    
    # Store the calculated total in our 1D array
    total_points[house_index] = house_total

# --- TASK 5: FILE HANDLING (SAVE) ---
# FIXME: Open the file "FinalResults.txt" in 'w' (write) mode
file = open("FinalResults.txt", "w")

for i in range(4):
    # Prepare the string to be saved
    line = house_names[i] + ", " + str(total_points[i]) + "\n"
    # FIXME: Write the 'line' variable to the file
    file.write(line)

# FIXME: Close the file
file.close()

print("\nResults saved to file successfully.")