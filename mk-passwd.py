import itertools
import subprocess
import os
from time import sleep
from colr import Colr as colr
import time


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
        sleep(0.5)
        Colors.green(" \n           AUTHOR: VARKMARKER \n")
        print(
            colr().hex("#ff8e35", " (", rgb_mode=True),
            colr().hex("#ff0066", "^", rgb_mode=True),
            colr().hex("#00ff8d", ".", rgb_mode=True),
            colr().hex("#ff0066", "^", rgb_mode=True),
            colr().hex("#ff8e35", ") ", rgb_mode=True),
            colr().hex("#ff0000", " Happy Cracking ", rgb_mode=True),
            colr().hex("#ff8e35", " (", rgb_mode=True),
            colr().hex("#ff0066", "^", rgb_mode=True),
            colr().hex("#00ff8d", ".", rgb_mode=True),
            colr().hex("#ff0066", "^", rgb_mode=True),
            colr().hex("#ff8e35", ") ", rgb_mode=True),
        )
        os.system("exit")

    def case_default():
        sleep(0.5)
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
        Colors.red("    ....Invalid Case....")


# generate wordlists keyword
def generate_passwords(min_length, max_length):
    characters = (
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    )

    for length in range(min_length, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            yield "".join(combination)

# Input from the user
def input_user():
    null = ""
    dash = null.center(52, "-")
    sleep(0.5)
    try:
        min_length = input(colr().hex("#6666ff", "\n Minimum Length    > "))
        min_length = int(min_length)
        sleep(0.5)
        max_length = input(colr().hex("#6666ff", " Maximum Length    > "))
        max_length = int(max_length)
        sleep(0.5)
        file_path = input(colr().hex("#6666ff", " File Name or Path > "))
        sleep(0.5)
        Colors.dark_rose("\n      ******* YOUR INPUT RESULt *******\n")
        print(
            colr().hex("#ff0000", "        Minimul Length : ", rgb_mode=True),
            colr().hex(
                "#00ff8d",
                f"{min_length}",
                rgb_mode=True,
            ),
            colr().hex("#ff0000", "\n        Maximum Length :", rgb_mode=True),
            colr().hex(
                "#00ff8d",
                f"{max_length}",
                rgb_mode=True,
            ),
            colr().hex("#ff0000", "\n        File :", rgb_mode=True),
            colr().hex(
                "#00ff8d",
                f"{file_path}",
                rgb_mode=True,
            ),
        )
        Colors.blue("\n Check the input is correct ? \n")
        answer = input(colr().hex("#6666ff", " y or n or e = exit > "))
        answer = answer.lower()
        if answer == "y" or answer == "yes":
            # calling the generate_wordlist
            null = ""
            dash = null.center(52, "-")
            Colors.red("\n      " + dash)
            print(
                colr().hex("#ff0000", "      |", rgb_mode=True),
                colr().hex(
                    "#00ff8d",
                    "=========== Password Storing Started ===========",
                    rgb_mode=True,
                ),
                colr().hex("#ff0000", "|", rgb_mode=True),
            )
            Colors.red("      " + dash)
            Colors.red("\n      " + dash)
            print(
                colr().hex("#ff0000", "      |", rgb_mode=True),
                colr().hex(
                    "#00ff8d",
                    f"++++++ Password Storing to >> {file_path} +++++",
                    rgb_mode=True,
                ),
                colr().hex("#ff0000", "|", rgb_mode=True),
            )
            Colors.red("      " + dash)
            # Saving the password generated by the function
            for password in generate_passwords(min_length, max_length):
                password = str(password)

                os.system(f"echo '{password}' >> {file_path}")
            Colors.red("\n      " + dash)
            print(
                colr().hex("#ff0000", "      |", rgb_mode=True),
                colr().hex(
                    "#00ff8d",
                    "=========== Password Stored Completed ==========",
                    rgb_mode=True,
                ),
                colr().hex("#ff0000", "|", rgb_mode=True),
            )
            Colors.red("      " + dash)
            choices()
        elif answer == "n" or answer == "no":
            input_user()
        elif answer == "e" or answer == "exit":
            Colors.red("\n Exit")
            exit()
        else:
            Operators.case_default()

    except ValueError:
        Operators.case_default()


# Main Choice
def choices():
    null = ""
    dash = null.center(107, "-")

    print(
        colr().hex(
            "#ff0000",
            """
::::    ::::  :::    :::              :::::::::     :::      ::::::::   ::::::::  :::       ::: :::::::::  
+:+:+: :+:+:+ :+:   :+:               :+:    :+:  :+: :+:   :+:    :+: :+:    :+: :+:       :+: :+:    :+: 
+:+ +:+:+ +:+ +:+  +:+                +:+    +:+ +:+   +:+  +:+        +:+        +:+       +:+ +:+    +:+ 
+#+  +:+  +#+ +#++:++   +#++:++#++:++ +#++:++#+ +#++:++#++: +#++:++#++ +#++:++#++ +#+  +:+  +#+ +#+    +:+ 
+#+       +#+ +#+  +#+                +#+       +#+     +#+        +#+        +#+ +#+ +#+#+ +#+ +#+    +#+ 
#+#       #+# #+#   #+#               #+#       #+#     #+# #+#    #+# #+#    #+#  #+#+# #+#+#  #+#    #+# 
###       ### ###    ###              ###       ###     ###  ########   ########    ###   ###   #########  """,
        ),
        colr().hex(
            "#00ff8d",
            "1.1",
        ),
    )

    Colors.blue("\n" + dash)
    null = ""
    dash = null.center(34, "-")
    Colors.blue("\n                                      " + dash)
    # Main Choice
    print(
        colr().hex("#0000ff", "                                      |", rgb_mode=True),
        colr().hex("#ff0000", " [1] MAKE-PASSWORD    [2] Exit", rgb_mode=True),
        colr().hex("#0000ff", "|", rgb_mode=True),
    )
    Colors.blue("                                      " + dash)
    sleep(0.5)
    # Main choice
    Colors.light_blue("\n Select One of the give option ?")

    try:
        choice = input(colr().hex("#ff0000", " > "))
        if choice == "1":
            input_user()

        elif choice == "2":
            Operators.exit()
        else:
            Operators.case_default()

    except KeyboardInterrupt:
        Colors.red("\n\n______KeyboardInterrupted_____")


# Call choice function
choices()
