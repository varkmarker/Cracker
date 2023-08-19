import itertools
import subprocess
import os
import tempfile
from time import sleep
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
        sleep(0.5)
        Colors.green(" \n AUTHOR: VARKMARKER \n")
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
        Colors.red("    ....Invalid option....")


# crack the handshake using the aircrack-ng tool
def aircrack_ng(handshake_path, wordlist_path):
    Colors.red("\n Starting Aircrack-ng")
    sleep(0.5)
    Colors.light_blue("")
    cmd = ["aircrack-ng", handshake_path, "-w", wordlist_path]
    subprocess.run(cmd)


# generate wordlists keyword
def generate_passwords(min_length, max_length):
    characters = (
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    )
    for length in range(min_length, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            yield "".join(combination)


def crack_handshake(handshake_file):
    try:
        try:
            Colors.blue("")
            cmd = [
                "aircrack-ng",
                "-w",
                "wordlist.txt",  # Read passwords from stdin
                handshake_file,
            ]
            result = subprocess.run(cmd)

        except KeyboardInterrupt:
            Colors.red("\n\n______KeyboardInterrupted_____")
        # Check if the process exited with an error
        if result.returncode != 0:
            print(f"Error occurred while cracking password: {result.stderr}")
        else:
            print(result.stdout)

    except Exception as e:
        print(f"An error occurred: {e}")


# Main Choice
def choices():
    null = ""
    dash = null.center(83, "-")

    print(
        colr().hex(
            "#ff0000",
            """    
::::::::  :::::::::      :::      ::::::::  :::    ::: :::::::::: :::::::::  
:+:    :+: :+:    :+:   :+: :+:   :+:    :+: :+:   :+:  :+:        :+:    :+: 
+:+        +:+    +:+  +:+   +:+  +:+        +:+  +:+   +:+        +:+    +:+ 
+#+        +#++:++#:  +#++:++#++: +#+        +#++:++    +#++:++#   +#++:++#:  
+#+        +#+    +#+ +#+     +#+ +#+        +#+  +#+   +#+        +#+    +#+ 
#+#    #+# #+#    #+# #+#     #+# #+#    #+# #+#   #+#  #+#        #+#    #+# 
 ########  ###    ### ###     ###  ########  ###    ### ########## ###    ### """,
        ),
        colr().hex(
            "#00ff8d",
            "1.1",
        ),
    )

    Colors.blue("\n" + dash)
    null = ""
    dash = null.center(35, "-")
    Colors.blue("\n               " + dash)
    print(
        colr().hex("#0000ff", "               |", rgb_mode=True),
        colr().hex("#ff0000", " [1] Cracker    [2] Aircrack-ng", rgb_mode=True),
        colr().hex("#0000ff", "|", rgb_mode=True),
    )
    print(
        colr().hex("#0000ff", "               |", rgb_mode=True),
        colr().hex("#ff0000", " [3] Exit", rgb_mode=True),
        colr().hex("#0000ff", "                      |", rgb_mode=True),
    )
    Colors.blue("               " + dash)
    sleep(0.5)
    Colors.light_blue("\n Select One of the give option ?")

    try:
        choice = input(colr().hex("#ff0000", " > "))
        if choice == "1":
            sleep(0.5)
            min_length = input(colr().hex("#6666ff", " Minimum Length > "))
            min_length = int(min_length)
            sleep(0.5)
            max_length = input(colr().hex("#6666ff", " Maximum Length > "))
            max_length = int(max_length)
            device_name = "Pocox4Pro5G"
            sleep(0.5)
            # Colors.red(
            #     "\n Copy this : handshake/handshake_POCOX4Pro5G_4A-B0-7F-21-B6-A3_2023-07-03T21-08-32.cap \n"
            # )
            # handshake_path = input(colr().hex("#6666ff", " Handshake Path > "))
            sleep(0.5)
            # calling the generate_wordlist
            for password in generate_passwords(min_length, max_length):
                password = str(password)

                os.system(
                    f"echo 'Device Name : {device_name}\nPassword : {password}' > wordlist.txt"
                )
                print(
                    colr().hex("#6666ff", "Checking Password: ", rgb_mode=True),
                    colr().hex("#ff0000", password, rgb_mode=True),
                )

            crack_handshake(
                "handshake/handshake_POCOX4Pro5G_4A-B0-7F-21-B6-A3_2023-07-03T21-08-32.cap"
            )
            choices()
        elif choice == "2":
            sleep(0.5)
            handshake_path = input(colr().hex("#6666ff", " Handshake Path > "))
            sleep(0.5)
            wordlist_path = input(colr().hex("#6666ff", " Wordlist Path > "))
            sleep(0.5)
            # call the aircrack-ng
            aircrack_ng(handshake_path, wordlist_path)
            choices()
        elif choice == "3":
            Operators.exit()
        else:
            Operators.case_default()

    except KeyboardInterrupt:
        Colors.red("\n\n______KeyboardInterrupted_____")


# Call choice function
choices()
