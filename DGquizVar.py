user_answerConfirm = str
user_score = 0
ans_check = True
ans_checkConfirm = True

question1 = ("Who was the Greek or Roman God of War? /n 1. Ares /n 2. Athena /n 3. Zues /n 4. Apollo")
question1_correct = 1

Q1 = [question1,question1_userAnswer,question1_correct]

question2 = ("What chemical element is diamond made of? /n 1. Silicon /n 2. Argon /n 3. Carbon /n 4. Boron")
question2_correct = 3

Q2 = [question2,question2_userAnswer,question2_correct]
Q3 = [question3,question3_userAnswer,question3_correct]

question3 = ("What is the name of the poker hand containing three of a kind and a pair? /n 1. Royal Flush /n 2. Full House /n 3. Three of a Kind /n 4. Two Pair")
question3_correct = 2

Q4 = [question4,question4_userAnswer,question4_correct]

question4 = ("What part of the body produces insulin? /n 1. Pancreas /n 2. Kidney /n 3. Brain /n 4. Liver")
question4_correct = 1

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
