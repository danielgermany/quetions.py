user_answer = str

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
    
while True:
    user_answer = input("Enter your answer without anything else.     ")
    try:
        if(user_answer == '1'):
            print("Your answer is incorrect")
            break
        elif(user_answer == '2'):
            print("Your answer is incorrect")
            break
        elif(user_answer == '3'):
            print("Your answer is correct")
            break
        elif(user_answer == '4'):
            print("Your answer is incorrect")
            break
    except:
        print("The answer you gave is either not one of the asnwer choices or no vaiable for use.")
