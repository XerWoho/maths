from colorama import Fore, Style
import msvcrt
import sys
import json
import os
import bcrypt
import uuid
import re
import getpass

username_pattern = r'^[a-zA-Z]+$'


from lib.exiting import exit
from modes.utils.streak_score import streak


class login_register:
    def __init__(self):
        self.options = ["Login", "Register", "Exit"]
        self.selected = 0
        self.uuid = None

        login_register.handle_movement(self)

    def display_menu(self):
        # Clear latest 3 lines from the Terminal
        sys.stdout.write("\033[{}A".format(3))
        sys.stdout.write("\033[J")

        for i, option in enumerate(self.options):
            if i == self.selected:
                print(Fore.LIGHTCYAN_EX + "> ", option + Style.RESET_ALL)
            else:
                print("  ", option)

    def handle_movement(self):
        while True:
            login_register.display_menu(self)

            key = msvcrt.getch()

            if key == b'\x03':
                print('Quiting...')
                exit()
            
            
            if key == b'H' and self.selected > 0:  # Up arrow key
                self.selected -= 1
            elif key == b'P' and self.selected < len(self.options) - 1:  # Down arrow key
                self.selected += 1
            elif key == b'\r':  # Enter key
                break
            else:
                continue
        
        if self.options[self.selected] == "Login":
            os.system('cls' if os.name == 'nt' else 'clear')
            login_register.login_method(self)
        elif self.options[self.selected] == "Register":
            os.system('cls' if os.name == 'nt' else 'clear')
            login_register.register_method(self)
        else:
            exit()



    def login_method(self):
            try:
                with open('users.json', 'r') as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError as e:
                        data = {
                            "users": []
                        }
            except FileNotFoundError:
                data = {
                    "users": []
                }

            
            user = {}

            
            
            while True:
                try:
                    self.username = input("Enter in your username ('.back' to get back):\n")
                    if self.username == ".back":
                        break
                except:
                    print('Quitting...')
                    exit()
            
                try:
                    user_password = getpass.getpass("Enter in your password:\n")
                except:
                    print("Qutting...")
                    exit()

                user_found = False
                for user in data["users"]:
                    if user["username"] == self.username:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        user_found = True  
                        user = user

                if not user_found:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Invalid credentials.")
                    continue
            
                if bcrypt.checkpw(user_password.encode('utf-8'), user["password"].encode('utf-8')):
                    self.uuid = user["uuid"]
                    break
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Invalid credentials.")
                    continue
    
            if self.username == ".back":
                return False

    def register_method(self):
        try:
            with open('users.json', 'r') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError as e:
                    data = {
                        "users": []
                    }
        except FileNotFoundError:
            data = {
                "users": []
            }
        

        while True:
            try:
                self.username = input("Enter in your username ('.back' to get back):\n")
            except:
                print('Quitting...')
                exit()
            
            if self.username == ".back":
                break
            elif not re.search(username_pattern, self.username):
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Username can only contain uppercase and lowercase letters!")
                continue
            
            already_taken = False

            for user in data["users"]:
                if user["username"] == self.username:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Username already taken.")
                    already_taken = True
                    

            if not already_taken:
                break                    

        if self.username == ".back":
            return False


        try:
            user_password = getpass.getpass("Enter in a secure password:\n")
        except:
            print('Quitting...')
            exit()
        
        hashed_password = bcrypt.hashpw(bytes(user_password, 'utf-8'), bcrypt.gensalt())

        os.system('cls' if os.name == 'nt' else 'clear')

        new_user = {
            'username': self.username, 
            'password': hashed_password.decode('utf-8'),
            'uuid': uuid.uuid4().hex,
            'longest_streak': 0,
            'history': [],
        }

        try:
            data["users"].append(new_user)
        except:
            data["users"] = []
            data["users"].append(new_user)

        with open('users.json', 'w') as file:
            json.dump(data, file, indent=4)

        self.uuid = new_user["uuid"]

        print(f"Alright {self.username}")