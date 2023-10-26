#Lola Weis
#CS-175
#Average and Grades Assignment


scores=[]
def calc_average(scores):
    total_score = sum(scores)
    average_score = total_score / 5
    return average_score

# Define a function to determine the letter grade based on the score
def determine_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80 and score < 90:
        return 'B'
    elif score >= 70 and score < 80:
        return 'C'
    elif score >= 60 and score < 70:
        return 'D'
    else:
        return 'F'

# Ask the user to enter five test scores
def enterScores():
    for x in range (5):
        print("Enter Score",x+1,": ")
        score=int(input())
        scores.append(score)
    return scores
scores=enterScores()

# Calculate the average score
average = calc_average(scores)

# Determine the letter grade for each score and display the results

another_calculation=True
while another_calculation==True:
        for i, score in enumerate(scores):
            grade = determine_grade(score)
            print(f"Score {i + 1}: {score}   {grade}")

        print(f"Average Score: {average}  {determine_grade(average)}")

        another_calculation = input("Enter 'yes' if you want to do another calculation: ").strip().lower()
        if another_calculation == 'yes':
            another_calculation = True
        else:
            another_calculation = False
            




