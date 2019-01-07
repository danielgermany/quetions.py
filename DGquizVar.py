user_answerConfirm = str
user_score = 0
ans_check = True
ans_checkConfirm = True

question1 = ("Who was the Greek or Roman God of War? /n 1. Ares /n 2. Athena /n 3. Zues /n 4. Apollo")
question1_correct = 1
question1_userAnswer = int

Q1 = [question1,question1_userAnswer,question1_correct]

question2 = ("What chemical element is diamond made of? /n 1. Silicon /n 2. Argon /n 3. Carbon /n 4. Boron")
question2_correct = 3
question2_userAnswer = int

Q2 = [question2,question2_userAnswer,question2_correct]

question3 = ("What is the name of the poker hand containing three of a kind and a pair? /n 1. Royal Flush /n 2. Full House /n 3. Three of a Kind /n 4. Two Pair")
question3_correct = 2
question3_userAnswer = int

Q3 = [question3,question3_userAnswer,question3_correct]

question4 = ("What part of the body produces insulin? /n 1. Pancreas /n 2. Kidney /n 3. Brain /n 4. Liver")
question4_correct = 1
question4_userAnswer = int

Q4 = [question4,question4_userAnswer,question4_correct]

question5 = ("In a standard pack of cards, which king is the only one to not have a moustache? /n 1. King of Spades /n 2. King of Clubs /n 3. King of Hearts /n 4. King of Diamonds")
question5_correct = 3
question5_userAnswer = int

Q5 = [question5,question5_userAnswer,question5_correct]

question6 = ("How many syllables make up a haiku? /n 1. 5 /n 2. 7 /n 3. 14 /n 4. 17")
question6_correct = 4
question6_userAnswer = int

Q6 = [question6,question6_userAnswer,question6_correct]

question7 = ("What is the standard unit of distance in the metric system? /n 1. Meter /n 2. Inches /n 3. Planck length /n 4. Kilometers")
question7_correct = 1
question7_userAnswer = int

Q7 = [question7,question7_userAnswer,question7_correct]

question8 = ("What is the official language of Brazil? /n 1. English /n 2. Spanish /n 3. Portuguese /n 4. French")
question8_correct = 3
question8_userAnswer = int 

Q8 = [question8,question8_userAnswer,question8_correct]

question9 = ("What superhero has been played by Michael Keaton, Val Kilmer, George Clooney and Christian Bale? /n 1. Superman /n 2. Captian America /n 3. Spider-Man /n 4. Batman")
question9_correct = 4
question9_userAnswer = int

Q9 = [question9,question9_userAnswer,question9_correct]

question10 = ("Does 2 + 2 = 5? /n 1. Yes /n 2. If you squint really hard /n 3. 1984 /n 4. idk")
question10_correct = 3
question10_userAnswer = int

Q10 = [question10,question10_userAnswer,question10_correct]

quiz = [Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10]

def question_Confirm(x):
    while ans_check and ans_checkConfirm: #Setting up loop
        ans_checkConfirm = False

        #Asks the user to answer
        print(quiz[x][1])
        print("Enter your answer without anything else.")
        quiz[x][2] = input()
        #Checks if answer given is valid or not
        if ans_check == True:
            try:
                user_answer = int(user_answer)
                if  1 < quiz[x][2] < 4:
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
                if quiz[x][2] == user_answerConfirm:
                    ans_checkConfirm = False
                else:
                    print("Your original answer and confirmed answer dosn't match.")
                    print("Returning you to the original questions")
                
            except ValueError:
                print("You answer was a string.")
                print("Please only enter 1, 2, 3, or 4 as viable answers.")
                ans_check = True

        ans_checkConfirm = True

def question_Grade(x):
    if quiz[x][2] == quiz[x][3]:
        user_score += 1

        


    
