print("WelCome to Quiz Test")

playing = input("Do you wanna play this quiz test? ").lower()

if playing != "yes":
    quit()
    
print("Okay, Lets play : ")  

score = 0 #initialization  
Question01 = input("Question 01. What is the sum of 2 & 3? ")
if Question01 == '5':
    print("Correct!")
    score += 1
else:
    print("Incorect answer!")
    
Question02 = input("Question 01. What is the sum of 6 & 3? ")
if Question02 == '9':
    print("Correct!")
    score += 1
else:
    print("Incorect answer!")        
    
    
print("Your score is: " + str(score))    
print("Your percentage of score is: " + str((score/2) * 100)) 