user_answer = str
user_score = 0
ans_check = True

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
    user_answer = input("Enter your answer without anything else.     ")
    #Checks if answer given is right or not
    try:
        user_answer = int(user_answer)
        if user_answer < 1:
            print("This isn't a valid answer")
            continue
        elif user_answer > 4:
            print("This isn't a valid answer")
            continue
        elif user_answer == 3:
            user_score +=1
            ans_check = False
            continue
    except ValueError:
        print("Please only enter whole numbers")

