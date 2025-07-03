# Username validator with Message formatting 

# 1. Ask username and convert it to lowercase 
# 2 . Remove any leading/tailing spaces.
# 3. Must be 5-12 characters long
# 4. Must not contain any digits 
# 5. Must not contain spaces in the middle 
# 6. Must contain only alphabets

username = input("Please enter your username: ")
username = username.lower().strip()

if len(username) < 5 or len(username) > 12 :
    print("Username length is not valid. ")
elif " " in username :
    print("Username must not contain any spaces. ")
elif  not username.isalpha() :
    print("Username should contain only alphabets (neither digits not special characters). ")
elif username.isalpha() :
    print(f"The username is: {username.title()}.")
else :
    print("Invalid")