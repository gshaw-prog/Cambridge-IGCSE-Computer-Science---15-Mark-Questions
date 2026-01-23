# Constants and setup
ClassSize = 30 # Example size, can be changed based on the actual class size

# Initializing the four parallel arrays as empty lists
# In a real scenario, these would be populated with data from a file or user input
StudentName = ['Roman','Ethan','Prem','Aurele','Mai Phong','Jorn','Fedor','Ilya','Alex','Hary','Wilson','Katie','Qintus','Mark','Sirach','Alex','Lukas']
CompSceMark = [23,22,14,17,15,12,22,19,17,21,26,27,28,12,16,25,26]
SceMark = [34,32,35,36,35,34,37,33,32,35,33,34,35,36,33,31,29]
MathsMark = [43,43,45,47,48,44,46,43,42,41,45,44,43,47,48,46,45]

# Initialize counters for class statistics
distinction_count = 0
merit_count = 0
pass_count = 0
fail_count = 0

# Loop through each student using the ClassSize variable
for i in range(ClassSize):
    # Calculate combined total mark for the 3 subjects
    total_mark = CompSceMark[i] + SceMark[i] + MathsMark[i]
    
    # Calculate average mark (3 subjects)
    average_mark = total_mark / 3
    
    # Determine the grade using selection
    if average_mark >= 70:
        grade = "distinction"
        distinction_count += 1
    elif average_mark >= 55:
        grade = "merit"
        merit_count += 1
    elif average_mark >= 40:
        grade = "pass"
        pass_count += 1
    else:
        grade = "fail"
        fail_count += 1
        
    # Output individual student results
    print("--------------------------------------")
    print("Student Name: ", StudentName[i])
    print("Combined Total Mark: ", total_mark)
    print("Average Mark: ", round(average_mark, 2))
    print("Grade Awarded: ", grade)

# Output final class statistics
print("\n--- Class Statistics Summary ---")
print("Number of Distinctions: ", distinction_count)
print("Number of Merits: ", merit_count)
print("Number of Passes: ", pass_count)
print("Number of Fails: ", fail_count)