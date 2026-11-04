# Aidan Pelletant
# November 4, 2026
# P4HW1
# Description: This program asks the user how many scores they want to enter,
# uses loops to validate each score (0-100), stores them in a list, 
# drops the lowest score, calculates the average manually, and displays the letter grade.

# Pseudocode:
# 1. Ask the user how many scores they would like to enter.
# 2. Initialize an empty list and a counter for valid scores.
# 3. Use a for loop to collect each score.
# 4. Use a while loop inside to validate that each score is between 0 and 100.
# 5. Append valid scores and keep a manual count of how many scores were added.
# 6. Find the lowest score and remove it from the list.
# 7. Manually calculate the sum of the remaining scores and divide by the new count.
# 8. Determine the letter grade and display all results.

# Ask user for the number of scores to enter
num_scores = int(input("How many scores do you want to enter? "))
score_list = []
valid_count = 0

# Loop to collect the specified number of scores
for i in range(1, num_scores + 1):
    score = float(input(f"Enter score #{i}: "))
    
    # Validation loop for scores between 0 and 100
    while score < 0 or score > 100:
        print("\nINVALID score entered!!!!")
        print("Score should be between 0 and 100.")
        score = float(input(f"Enter score #{i} again: "))
        
    # Add valid score to the list and increment manual count
    score_list.append(score)
    valid_count += 1

print("-" * 40)

# Results Calculations
lowest_score = min(score_list)
score_list.remove(lowest_score)
valid_count -= 1  # Subtract 1 because we removed the lowest score

# Calculate average of the modified list manually without built-in len()
total_sum = 0
for s in score_list:
    total_sum += s

if valid_count > 0:
    score_average = total_sum / valid_count
else:
    score_average = 0.0

# Determine letter grade
if score_average >= 90:
    letter_grade = 'A'
elif score_average >= 80:
    letter_grade = 'B'
elif score_average >= 70:
    letter_grade = 'C'
elif score_average >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Display Results
print("-----------------Results-----------------")
print(f"Lowest score : {lowest_score}")
print(f"Modified List : {score_list}")
print(f"Scores Average: {score_average:.2f}")
print(f"Grade : {letter_grade}")
print("-----------------------------------------")