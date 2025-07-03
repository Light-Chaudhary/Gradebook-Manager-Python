# Python 🐍 Simple Quiz App

name = input("Please! Enter your name: ")

if name.isalpha() and len(name) >= 3 and len(name) <=15 :
    score = 0
    print(f"Welcome, {name.title()}, Lets start our quiz 🐍")
    firstquestion = input("\nWhat is the capital city of Nepal?\nA. Kathmandu\nB. Kritipur\nC. Lalitpur\n")
    if firstquestion.lower() == "a" :
        print("\nYou first answer is correct. 😁 ")
        score+=1
    else :
        print("\nWrong")
    secondquestion = input("\nWhich company gadgets are better?\nA. Apple\nB. Samsung\nC. Microsoft\n")
    if secondquestion.lower() == "a" : 
        print("\nYour second answer is also correct. 😁 ")
        score+=1
    else :
        print("\nWrong")
    thirdquestion =  input("What is the tallest mountain in the world?\nA. Mount Everest\nB. Mount Fuji\nC. Mount K2\n")
    if thirdquestion.lower() == "a" :
        print("\nYour all answer was correct. 😁 ")
        score+=1
        print(f"Congratulation👏🏻, {name.title()} you have answer {score} of 3 question 🎉🎊")
        if score == 3:
            print("You won 7 crore🏅")
        else :
            print("Try next time😭")
    else :
        print("\nWrong! ")
else :
    print("Not valid")