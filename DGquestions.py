user_answer = str
user_answerConfirm = str
user_score = 0
ans_check = True
ans_checkConfirm = True



while ans_check and ans_checkConfirm: #Setting up loop
    ans_checkConfirm = False
    #Asks the user a question
    print("--------------------------------------------------------")
    print("What is 9 squared?")
    #Gives user an example on how to use the program
    print("Press the number corresponding to the asnwer.")
    print("For example if you believe the answer to be 3 then press 1 on your keyboard.")
    #Gives user answers to choose from
    print("1. 3")
    print("2. 9")
    print("3. 81")
    print("4. 18")

    #Asks the user to answer
    print("Enter your answer without anything else.")
    user_answer = input()
    #Checks if answer given is valid or not
    if ans_check == True:
        try:
            user_answer = int(user_answer)
            if user_answer < 1:
                print("This isn't a valid answer, this number was either 0 or a negative number.")
                print("Please only enter 1, 2, 3, or 4 as viable answers.")
                ans_checkConfirm = False               
            elif user_answer > 4:
                print("This isn't a valid answer, this number was higher than 4.")
                print("Please only enter 1, 2, 3, or 4 as viable answers.")
                ans_checkConfirm = False
            else:
                ans_check = False
                ans_checkConfirm = True
        except ValueError:
            print("You answer was a string.")
            print("Please only enter 1, 2, 3, or 4 as viable answers.")
            ans_checkConfirm = False
            
    if ans_checkConfirm == True:
        #Asks the user to answer confirmation question.
        print("Confirm that your answer is ", user_answer, " by entering you answer again.")
        user_answerConfirm = input()
        try:
            user_answerConfirm = int(user_answerConfirm)
            if user_answerConfirm < 1:
                print("This isn't a valid answer, this number was either 0 or a negative number.")
                print("Please only enter 1, 2, 3, or 4 as viable answers.")
                ans_check = True

            elif user_answerConfirm > 4:
                print("This isn't a valid answer, this number was higher than 4.")
                print("Please only enter 1, 2, 3, or 4 as viable answers.")
                ans_check = True
                
            elif user_answerConfirm == user_answer:
                ans_checkConfirm = False
                print("Your answer has been confirmed, proceeding to the next question.")
                if user_answer == 3:
                    user_score+=1              
            else:
                print("Your original answer and confirmed answer dosn't match.")
                print("Returning you to the orignal question")
                ans_check = True
        except ValueError:
            print("You answer was a string.")
            print("Please only enter 1, 2, 3, or 4 as viable answers.")
            ans_check = True

    ans_checkConfirm = True

