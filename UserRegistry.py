import getpass, random, secrets,re

#function that generates a random username based on 10 world renowned authors and generates a random secure password and the options to customize it
class user_profile():
    
    #function that validates the username by criteria described below 
    def validate_username(username):
        '''        
User Name Creation Rules:  
1. Length: Usually between 3-32 characters
2. Characters: Letters, numbers, underscores, hyphens
3. Special characters: Avoid (!, $, %, etc.)
4. Case sensitivity: Often case-insensitive
5. Uniqueness: Must be unique within the system '''
        pattern = r'^[a-zA-Z0-9_-]{3,32}$'
        return bool(re.match(pattern, username))
     
 #function that validates password based on criteria   
    def validate_password(password):
        '''
Password Creation Rules:
1. Minimum length: At least 8 characters
2. Uppercase letters: At least one
3. Lowercase letters: At least one
4. Numbers: At least one
5. Special characters: At least one (@,!,%, etc.)'''
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        return bool(re.match(pattern, password))
    def check_common_passwords(password):
        common_password_list = ["qwerty","password"]
        length = len(password)
        if password in common_password_list and length <8 :
            return False
        else:
            return True
    def create():
        author_name_list = (
                            "Stephen", "King","Jane", "Austen","William", "Shakespeare",
                            "George", "RR" ,"Martin","J", "RR", "Tolkien","Charles", "Dickens",
                            "Virginia", "Woolf","Edgar", "Allan", "Poe","Leo", "Nikolayevich",
                            "Tolstoy","Fyodor", "Mikhailovich", "Dostoevsky")
        username = f"{random.choice(author_name_list)}{random.choice(author_name_list)}{random.randint(0,100)}"
        print(f"""
A randomly generated username was created for you,              
--------------------------------------------------
Username = {username} 
This can be changed later in the settings.
--------------------------------------------------              

Would you like to change this now or continue?""")
        user_input = str(input()).lower()
 
        #While loop to check input validation of username    
        while True:

            if user_input in ['change','yes']:
                    username = (input("""
-----------------------------------------------------------
User Name Creation Rules:                                     
Length: Typically 3-32 characters.
Allowed characters: Letters, numbers, underscores, hyphens.
Avoid special characters: !, $, %, etc.
Case sensitivity: Often case-insensitive.
Uniqueness: Must be unique within the system.                                 
-----------------------------------------------------------"""))
                    if user_profile.validate_username(username):
                        print(f"{username} is a valid Username\n")
                        break
                    else:
                        print("Invalid username. Please use letters, numbers, underscores, and hyphens.")
            elif user_input in ['continue','no']:
                print(f"Your username is {username}")  
                break                  
            else:
                print(f"{user_input} is not a correct selection, check spelling and options, please try again")   
                user_profile.create()
        password = secrets.token_urlsafe(12)
        
        print(f"""
A randomly generated password was created for you,              
--------------------------------------------------
Password = {password} 
This can be changed later in the settings.
--------------------------------------------------              

Would you like to change this now or continue?""")
        user_input = input().lower()
 
#While loop to check input validation of password    
        while True:

            if user_input in ['change','yes']:
                password = getpass.getpass("""
--------------------------------------------------
Password Creation Rules:
1. Minimum length: At least 8 characters
2. Uppercase letters: At least one
3. Lowercase letters: At least one
4. Numbers: At least one
5. Special characters: At least one (@,!,%, etc.)       
-------------------------------------------------
characters will not be shown as you type:\n""")
                if user_profile.validate_password(password) and user_profile.check_common_passwords(password):
                    
                        print(f"{password} is a valid Password\n")
                        break
                
                else:
                    print("Password must contain uppercase, lowercase, digits, and special characters.")
                    
            elif user_input in ['continue', 'no']:
                print(f"Your password is {password}")
                break
            else:
                print(f"{user_input} is not a correct selection, check spelling and options, please try again")  
         
         
         
                             
        return username, password
        

            
user_test = user_profile.create()
print(user_test)            
            
            
            
            
            
            
