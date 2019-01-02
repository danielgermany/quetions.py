user_answerConfirm = str
user_score = 0
ans_check = True
ans_checkConfirm = True

Q1 = [question1,question1_userAnswer,question1_correct]
Q2 = [question2,question2_userAnswer,question2_correct]
Q3 = [question3,question3_userAnswer,question3_correct]
Q4 = [question4,question4_userAnswer,question4_correct]
Q5 = [question5,question5_userAnswer,question5_correct]
Q6 = [question6,question6_userAnswer,question6_correct]
Q7 = [question7,question7_userAnswer,question7_correct]
Q8 = [question8,question8_userAnswer,question8_correct]
Q9 = [question9,question9_userAnswer,question9_correct]
Q10 = [question10,question10_userAnswer,question10_correct]

quiz = [Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10]

def question_Confirm():
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
        quiz[0][1] = input()
        #Checks if answer given is valid or not
        if ans_check == True:
            try:
                user_answer = int(user_answer)
                if  1 < quiz[0][1] < 4:
                    ans_check = False
                ans_checkConfirm = True
                else:
                    print("Please only enter 1, 2, 3, or 4 as viable answers.")
                    ans_checkConfirm = False
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
                if quiz[0][1] == quiz[0][2]:
                    ans_checkConfirm = False
                else:
                    print("Your original answer and confirmed answer dosn't match.")
                    print("Returning you to the original questions")
                
            except ValueError:
                print("You answer was a string.")
                print("Please only enter 1, 2, 3, or 4 as viable answers.")
                ans_check = True

        ans_checkConfirm = True
