# Aidan Pelletant
# November 1, 2026
# P4HW1
# Description: This program asks the user how many scores they want to enter, 
#              collects the scores using loops with input validation (0-100), 
#              stores them in a list, drops the lowest score, calculates the average, 
#              and determines the corresponding letter grade.
#
# Pseudocode:
# 1. Ask the user how many scores they want to enter.
# 2. Make an empty list (score_list).
# 3. Use a FOR loop to collect each score based on the user's requested quantity:
#    a. While input is invalid (not between 0 and 100), display an error message and re-prompt.
#    b. Once valid, append the score to score_list.
# 4. After collecting all scores:
#    a. Find the lowest score in the list.
#    b. Remove the lowest score from the list.
#    c. Calculate the average of the remaining scores in the modified list.
#    d. Determine the letter grade based on the average (A, B, C, D, or F).
# 5. Display the lowest score, modified score list, average, and letter grade.
# -----------------------------------------------------------------------------

def main():
    # Ask user for the number of scores to enter
    num_scores = int(input("How many scores do you want to enter? "))
    
    score_list = []
    
    # Loop to collect the specified number of scores
    for i in range(1, num_scores + 1):
        score = float(input(f"Enter score #{i}: "))
        
        # Validation loop for scores between 0 and 100
        while score < 0 or score > 100:
            print("\nINVALID score entered!!!!")
            print("Score should be between 0 and 100.")
            score = float(input(f"Enter score #{i} again: "))
            
        # Add valid score to the list
        score_list.append(score)
        
    print("-" * 40)
    
    # Results Calculations
    lowest_score = min(score_list)
    score_list.remove(lowest_score)
    
    # Calculate average of the modified list
    if len(score_list) > 0:
        score_average = sum(score_list) / len(score_list)
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
    print(f"Lowest score  : {lowest_score}")
    print(f"Modified List : {score_list}")
    print(f"Scores Average: {score_average:.2f}")
    print(f"Grade         : {letter_grade}")
    print("-----------------------------------------")

if __name__ == "__main__":
    main()