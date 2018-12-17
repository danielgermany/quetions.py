user_answer = str
user_answerConfirm = str
user_score = 0
ans_check = True
ans_checkConfirm = True

#Asks the user a question
print("What is 9 squared?")
#Gives user an example on how to use the program
print("Press the number corresponding to the asnwer.")
print("For example if you believe the answer to be 3 then press 1 on your keyboard.")
#Gives user answers to choose from
print("1. 3")
print("2. 9")
print("3. 81")
print("4. 18")

while ans_check: #Setting up loop
    #Asks the user to answer
    print("Enter your answer without anything else.")
    user_answer = input()
    #Checks if answer given is right or not
    try:
        user_answer = int(user_answer)
        if user_answer < 1:
            print("This isn't a valid answer, this number was either 0 or a negative number.")
            print("Please only enter 1, 2, 3, or 4 as viable answers.")
            continue
        elif user_answer > 4:
            print("This isn't a valid answer, this number was higher than 4.")
            print("Please only enter 1, 2, 3, or 4 as viable answers.")
            continue
        else:
            ans_check = False
    except ValueError:
        print("You answer was a string.")
        print("Please only enter 1, 2, 3, or 4 as viable answers.")


while ans_checkConfirm: #Setting up loop for confirmation of asnwer
    #Asks the user to answer confirmation question.
    print("Confirm that your answer is ", user_answer, " by entering you answer again.")
    user_answerConfirm = input()
    try:
        user_answerConfirm = int(user_answerConfirm)
        if user_answerConfirm < 1:
            print("This isn't a valid answer, this number was either 0 or a negative number.")
            print("Please only enter 1, 2, 3, or 4 as viable answers.")
            continue
        elif user_answerConfirm> 4:
            print("This isn't a valid answer, this number was higher than 4.")
            print("Please only enter 1, 2, 3, or 4 as viable answers.")
            continue
        elif user_answerConfirm == user_answer:
            ans_checkConfirm = False
            print("Your answer has been confirmed, proceeding to the next question.")
            continue
        else:
            print("Your original answer and confirmed answer dosn't match.")
    except ValueError:
        print("You answer was a string.")
        print("Please only enter 1, 2, 3, or 4 as viable answers.")



