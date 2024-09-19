import getpass, random, secrets, re

# Class that generates a random username and secure password with customization options
class UserProfile:

    # Function to validate the username based on the given rules
    @staticmethod
    def validate_username(username):
        """
        User Name Creation Rules:
        1. Length: Between 3-32 characters
        2. Characters: Letters, numbers, underscores, hyphens
        3. Special characters: Avoid (!, $, %, etc.)
        4. Case sensitivity: Often case-insensitive
        5. Uniqueness: Must be unique within the system
        """
        pattern = r'^[a-zA-Z0-9_-]{3,32}$'
        return bool(re.match(pattern, username))

    # Function to validate the password based on the given rules
    @staticmethod
    def validate_password(password):
        """
        Password Creation Rules:
        1. Minimum length: At least 8 characters
        2. Uppercase letters: At least one
        3. Lowercase letters: At least one
        4. Numbers: At least one
        5. Special characters: At least one (@, !, %, etc.)
        """
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        return bool(re.match(pattern, password))

    # Function to check if the password is common and shorter than 8 characters
    @staticmethod
    def check_common_passwords(password):
        common_password_list = ["qwerty", "password"]
        return password not in common_password_list or len(password) >= 8

    # Function to create a random username and secure password, with the option for customization
    @staticmethod
    def create():
        author_name_list = (
            "Stephen", "King", "Jane", "Austen", "William", "Shakespeare",
            "George", "RR", "Martin", "J", "RR", "Tolkien", "Charles", "Dickens",
            "Virginia", "Woolf", "Edgar", "Allan", "Poe", "Leo", "Nikolayevich",
            "Tolstoy", "Fyodor", "Mikhailovich", "Dostoevsky"
        )

        # Generate a random username
        username = f"{random.choice(author_name_list)}{random.choice(author_name_list)}{random.randint(0,100)}"
        
        print(f"""
A randomly generated username was created for you:
--------------------------------------------------
Username = {username}
This can be changed later in the settings.
--------------------------------------------------
Would you like to change this now or continue? (Type 'change' to modify or 'continue' to keep)
""")
        
        user_input = input().lower()

        # Loop to validate the username input
        while True:
            if user_input in ['change', 'yes']:
                username = input("""
-----------------------------------------------------------
User Name Creation Rules:
Length: Typically 3-32 characters.
Allowed characters: Letters, numbers, underscores, hyphens.
Avoid special characters: !, $, %, etc.
-----------------------------------------------------------
Please enter a new username:
""")
                if UserProfile.validate_username(username):
                    print(f"{username} is a valid Username\n")
                    break
                else:
                    print("Invalid username. Please use letters, numbers, underscores, and hyphens.")
            elif user_input in ['continue', 'no']:
                print(f"Your username is {username}")
                break
            else:
                print(f"'{user_input}' is not a valid selection, please try again.")
                user_input = input().lower()

        # Generate a random password
        password = secrets.token_urlsafe(12)
        
        print(f"""
A randomly generated password was created for you:
--------------------------------------------------
Password = {password}
This can be changed later in the settings.
--------------------------------------------------
Would you like to change this now or continue? (Type 'change' to modify or 'continue' to keep)
""")
        
        user_input = input().lower()

        # Loop to validate the password input
        while True:
            if user_input in ['change', 'yes']:
                password = getpass.getpass("""
--------------------------------------------------
Password Creation Rules:
1. Minimum length: At least 8 characters
2. Uppercase letters: At least one
3. Lowercase letters: At least one
4. Numbers: At least one
5. Special characters: At least one (@, !, %, etc.)
--------------------------------------------------
characters will not be shown as you type:
""")
                if UserProfile.validate_password(password) and UserProfile.check_common_passwords(password):
                    print(f"{password} is a valid Password\n")
                    break
                else:
                    print("Invalid password. It must contain uppercase, lowercase, digits, and special characters.")
            elif user_input in ['continue', 'no']:
                print(f"Your password is {password}")
                break
            else:
                print(f"'{user_input}' is not a valid selection, please try again.")
                user_input = input().lower()

        return username, password

# Test the user profile creation
user_test = UserProfile.create()
print(user_test)
