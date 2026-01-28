# Initialize arrays and variables
# MemberName and TestScores are pre-populated or initialized as empty
MemberName = [""] * 20
TestScores = [[0] * 3 for _ in range(20)] # 2D array: 20 rows, 3 columns
TotalScore = [0] * 20

grand_total = 0
highest_total = -1
winner_name = ""

# Main loop to process each of the 20 members
for i in range(20):
    # Input member name
    MemberName[i] = input(f"Enter name for member {i+1}: ")
    
    current_member_sum = 0
    
    # Nested loop to input and validate 3 test scores per member
    for j in range(3):
        valid_input = False
        while not valid_input:
            score = int(input(f"  Enter score for test {j+1} (0-100): "))
            
            # Validation: check if score is between 0 and 100 inclusive
            if score >= 0 and score <= 100:
                TestScores[i][j] = score
                current_member_sum = current_member_sum + score
                valid_input = True
            else:
                print("  Invalid score. Please enter a value between 0 and 100.")
                
    # Store the member's total score in the 1D array
    TotalScore[i] = current_member_sum
    
    # Add to grand total for the club average calculation later
    grand_total = grand_total + current_member_sum
    
    # Check if this member has the highest score so far
    if current_member_sum > highest_total:
        highest_total = current_member_sum
        winner_name = MemberName[i]

# Calculations after all data is collected
average_club_score = grand_total / 20

# Final Outputs
print("\n--- Fitness Challenge Results ---")
print(f"Average score for the club: {average_club_score}")
print(f"Highest scoring member: {winner_name} with {highest_total} points")