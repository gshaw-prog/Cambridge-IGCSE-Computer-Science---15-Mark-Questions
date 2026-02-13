# --- INITIALIZATION ---
# SYLLABUS REF: 2.2.1 Programming concepts (1D and 2D Arrays)
# Using a 1D array for names to map indices to human-readable labels.
house_names = ["Red", "Blue", "Green", "Yellow"]

# SYLLABUS REF: 2.2.1 Declare and initialize 2D arrays
# We use a list comprehension to create a grid (4 rows for houses, 5 columns for events).
# It is vital to initialize to 0 to prevent "garbage" data affecting calculations.
score_table = [[0 for event in range(5)] for house in range(4)]

# SYLLABUS REF: 1D array to store calculated totals
total_points = [0, 0, 0, 0]

# --- TASK 2: INPUT & VALIDATION ---
# SYLLABUS REF: 2.2.2 Nested Loops (FOR...TO...NEXT)
# The outer loop handles the Row (House), the inner loop handles the Column (Event).
for house_index in range(4):
    print(f"\n--- Entering scores for House: {house_names[house_index]} ---")
    
    for event_index in range(5):
        # SYLLABUS REF: 2.1.1 Validation Checks (Range Check)
        # We use a WHILE loop for validation. The loop continues until data is valid.
        valid_input = False
        while not valid_input:
            try:
                # SYLLABUS REF: 2.2.1 Data types (Integer)
                score = int(input(f"Enter score for Event {event_index + 1} (0-10): "))
                
                # IGCSE Range Check: Ensures score is within the boundary (0 and 10).
                if score >= 0 and score <= 10:
                    score_table[house_index][event_index] = score
                    valid_input = True
                else:
                    print("Error: Score must be between 0 and 10.")
            except ValueError:
                # SYLLABUS REF: 2.3.1 Robustness (Preventing crashes from non-numeric input)
                print("Error: Please enter a whole number.")

# --- TASK 3: CALCULATION (SUMMING) ---
# SYLLABUS REF: 2.1.2 Totalling and Counting
for house_index in range(4):
    row_sum = 0 # This is an 'accumulator' variable
    for event_index in range(5):
        # Adding each event score in the row to the house total.
        row_sum += score_table[house_index][event_index]
    
    # Store the final total in the corresponding index of the 1D array.
    total_points[house_index] = row_sum

# --- TASK 4: FINDING THE MAXIMUM ---
# SYLLABUS REF: 2.1.2 Standard Algorithm (Finding Max/Min)
highest_score = total_points[0] # Assume the first house is the winner
winner_index = 0

for i in range(1, 4):
    if total_points[i] > highest_score:
        highest_score = total_points[i]
        winner_index = i

print(f"\nWINNER: {house_names[winner_index]} with {highest_score} points!")

# --- TASK 5: FILE HANDLING (WRITE) ---
# SYLLABUS REF: 2.2.3 File Handling (Open, Write, Close)
try:
    # 'w' mode (Write) is used to create the file or overwrite existing content.
    file = open("FinalResults.txt", "w")
    for i in range(4):
        # Converting data to string and adding a newline (\n).
        data_string = f"{house_names[i]}, {total_points[i]}\n"
        file.write(data_string)
    
    # SYLLABUS REF: 2.2.3 Always close the file to save the buffer to disk.
    file.close()
    print("\nData successfully saved to FinalResults.txt")
except IOError:
    print("Error: Could not write to file.")

# --- TASK 6: FILE HANDLING (READ) ---
# SYLLABUS REF: 2.2.3 Reading from a file until EOF (End Of File)
print("\n--- Verifying Saved Records ---")
try:
    # 'r' mode (Read) allows the program to access data without changing it.
    file = open("FinalResults.txt", "r")
    # Python's 'for line in file' is the equivalent of 'WHILE NOT EOF' in pseudocode.
    for line in file:
        print(line.strip()) # .strip() removes the newline character for display.
    file.close()
except FileNotFoundError:
    print("Error: The file does not exist.")