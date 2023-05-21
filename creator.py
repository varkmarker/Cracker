import random
import string
import os
import time
from colr import Colr as colr


# Color's functions
class Colors:
    def red(data):
        print(colr().hex("#ff0000", data, rgb_mode=True))

    def rose(data):
        print(colr().hex("#ff0066", data, rgb_mode=True))

    def green(data):
        print(colr().hex("#00ff8d", data, rgb_mode=True))

    def gnome_green(data):
        print(colr().hex("#2ed1b4", data, rgb_mode=True))

    def yellow_green(data):
        print(colr().hex("#a8c836", data, rgb_mode=True))

    def dark_orange(data):
        print(colr().hex("#cf301b", data, rgb_mode=True))

    def light_gnome(data):
        print(colr().hex("#00ffc4", data, rgb_mode=True))

    def yellow_green(data):
        print(colr().hex("#7ed666", data, rgb_mode=True))

    def violet(data):
        print(colr().hex("#cc33ff", data, rgb_mode=True))

    def light_green(data):
        print(colr().hex("#21ff00", data, rgb_mode=True))

    def orange(data):
        print(colr().hex("#ff8e35", data, rgb_mode=True))

    def yellow(data):
        print(colr().hex("#fff300", data, rgb_mode=True))

    def sky_blue(data):
        print(colr().hex("#00ccff", data, rgb_mode=True))

    def blue(data):
        print(colr().hex("#0000ff", data, rgb_mode=True))

    def cream(data):
        print(colr().hex("#ff9999", data, rgb_mode=True))

    def dark_rose(data):
        print(colr().hex("#cc0066", data, rgb_mode=True))

    def dark_red(data):
        print(colr().hex("#cc0000", data, rgb_mode=True))

    def dark_green(data):
        print(colr().hex("#009933", data, rgb_mode=True))

    def light_blue(data):
        print(colr().hex("#6666ff", data, rgb_mode=True))


# Operators
class Operators:
    def exit():
        time.sleep(0.5)
        Colors.light_blue(
            " \n If this script saves you time. You can give a star on GitHub"
        )
        time.sleep(0.5)
        Colors.light_blue(
            " \n If any error you can post the issue on the GitHub page: https://github.com/varkmarker/Password_creater/issues"
        )
        time.sleep(0.5)
        Colors.light_blue(
            f" \n If you have any suggestions about this tool you can contact me on Twitter."
        )
        time.sleep(0.5)
        Colors.light_blue(" \n Twitter link: https://twitter.com/varkmarker")
        time.sleep(0.5)
        Colors.light_blue(" \n AUTHOR: VARKMARKER \n")
        os.system("exit")

    def case_default():
        time.sleep(0.5)
        print(
            colr().hex(
                "#00ffff",
                """                 (__) 
                 (oo) 
           /------\/ 
          / |    ||   
         *  /\---/\ 
            ~~   ~~""",
            )
        )
        Colors.red("    ....Invalid option....")


# Main Choice
def choice():
    print(
        colr().hex(
            "#ff0000",
            """\n    
  #####                                           
 #     # #####  ######   ##   #####  ####  #####  
 #       #    # #       #  #    #   #    # #    # 
 #       #    # #####  #    #   #   #    # #    # 
 #       #####  #      ######   #   #    # #####  
 #     # #   #  #      #    #   #   #    # #   #  
  #####  #    # ###### #    #   #    ####  #    #""",
        ),
        colr().hex(
            "#00ff8d",
            "1.0",
        ),
    )
    Colors.light_blue(
        "\n [1] ASCII_LOWERCASE(abcd)                             [2] ASCII_UPPERCASE(ABCD)"
    )
    Colors.light_blue(
        " [3] PUNCTUATION(#$%&)                                 [4] DIGITS(123)"
    )
    Colors.light_blue(
        " [5] HEXDIGITS(Digits+lower and uppercase alphabet)    [6] ASCII_LETTERS(lowercase and uppercase alphabet)"
    )
    Colors.light_blue(" [7] EXIT")
    time.sleep(0.5)
    Colors.red("\n Select the type of password key's")
    time.sleep(0.5)
    choice = input(colr().hex("#ff0000", " > "))
    try:
        choice = int(choice)
    except ValueError:
        Operators.case_default()
    if choice == 1:
        time.sleep(0.5)
        minimum = input(colr().hex("#6666ff", " Minimum Length > "))
        minimum = int(minimum)
        time.sleep(0.5)
        maximum = input(colr().hex("#6666ff", " Maximum Length > "))
        maximum = int(maximum)
        time.sleep(0.5)
        count = input(colr().hex("#6666ff", " Maximum Count > "))
        count = int(count)
        time.sleep(0.5)
        filename = input(colr().hex("#6666ff", " Enter your filename > "))
        filename = str(filename)
        time.sleep(0.5)
        Generate.generate_password(
            minimum, maximum, string.ascii_lowercase, count, filename
        )
    elif choice == 2:
        time.sleep(0.5)
        minimum = input(colr().hex("#6666ff", " Minimum Length > "))
        minimum = int(minimum)
        time.sleep(0.5)
        maximum = input(colr().hex("#6666ff", " Maximum Length > "))
        maximum = int(maximum)
        time.sleep(0.5)
        count = input(colr().hex("#6666ff", " Maximum Count > "))
        count = int(count)
        time.sleep(0.5)
        filename = input(colr().hex("#6666ff", " Enter your filename > "))
        filename = str(filename)
        time.sleep(0.5)
        Generate.generate_password(
            minimum, maximum, string.ascii_uppercase, count, filename
        )
    elif choice == 3:
        time.sleep(0.5)
        minimum = input(colr().hex("#6666ff", " Minimum Length > "))
        minimum = int(minimum)
        time.sleep(0.5)
        maximum = input(colr().hex("#6666ff", " Maximum Length > "))
        maximum = int(maximum)
        time.sleep(0.5)
        count = input(colr().hex("#6666ff", " Maximum Count > "))
        count = int(count)
        time.sleep(0.5)
        filename = input(colr().hex("#6666ff", " Enter your filename > "))
        filename = str(filename)
        time.sleep(0.5)
        Generate.generate_password(
            minimum, maximum, string.punctuation, count, filename
        )
    elif choice == 4:
        time.sleep(0.5)
        minimum = input(colr().hex("#6666ff", " Minimum Length > "))
        minimum = int(minimum)
        time.sleep(0.5)
        maximum = input(colr().hex("#6666ff", " Maximum Length > "))
        maximum = int(maximum)
        time.sleep(0.5)
        count = input(colr().hex("#6666ff", " Maximum Count > "))
        count = int(count)
        time.sleep(0.5)
        filename = input(colr().hex("#6666ff", " Enter your filename > "))
        filename = str(filename)
        time.sleep(0.5)
        Generate.generate_password(minimum, maximum, string.digits, count, filename)
    elif choice == 5:
        time.sleep(0.5)
        minimum = input(colr().hex("#6666ff", " Minimum Length > "))
        minimum = int(minimum)
        time.sleep(0.5)
        maximum = input(colr().hex("#6666ff", " Maximum Length > "))
        maximum = int(maximum)
        time.sleep(0.5)
        count = input(colr().hex("#6666ff", " Maximum Count > "))
        count = int(count)
        time.sleep(0.5)
        filename = input(colr().hex("#6666ff", " Enter your filename > "))
        filename = str(filename)
        time.sleep(0.5)
        Generate.generate_password(minimum, maximum, string.hexdigits, count, filename)
    elif choice == 6:
        time.sleep(0.5)
        minimum = input(colr().hex("#6666ff", " Minimum Length > "))
        minimum = int(minimum)
        time.sleep(0.5)
        maximum = input(colr().hex("#6666ff", " Maximum Length > "))
        maximum = int(maximum)
        time.sleep(0.5)
        count = input(colr().hex("#6666ff", " Maximum Count > "))
        count = int(count)
        time.sleep(0.5)
        filename = input(colr().hex("#6666ff", " Enter your filename > "))
        filename = str(filename)
        time.sleep(0.5)
        Generate.generate_password(
            minimum, maximum, string.ascii_letters, count, filename
        )
    elif choice == 7:
        Operators.exit()


# Generate's password form here
class Generate:
    def generate_password(minilength, maxlength, type, count, filename):
        time.sleep(0.5)
        Colors.red(" PASSWORD WORDLIST CREATING ......")
        time.sleep(0.5)
        for length in range(minilength, maxlength + 1):
            for i in range(1, count + 1):
                characters = type
                password = "".join(random.choice(characters) for _ in range(length))
                print(f"{i} : {password}")
                os.system(f"echo {password} >> {filename}.txt")
        time.sleep(0.5)
        Colors.red(" PASSWORD CREATED SUCCESSFULLY")
        time.sleep(0.5)
        choice()


# Call choice function
choice()
