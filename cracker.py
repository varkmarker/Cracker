import hashlib, os, pdfplumber, colorama, time, random, zipfile, msoffcrypto, io, threading, chardet
from time import sleep
from rarfile import RarFile
from itertools import product
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


# generating password or read wordlist file for the attack
class Generate:
    # generating password for the attack
    def BrutForce(characters, min_length, max_length):
        for length in range(min_length, max_length + 1):
            for combination in product(characters, repeat=length):
                yield "".join(combination)

    # Directory reader
    def directory(file_name_or_path):
        f = open(file_name_or_path, "rb")
        pass_list = f.readlines()
        f.close()
        for i in pass_list:
            detection = chardet.detect(i)
            encoding = detection["encoding"]
            try:
                yield i.decode(encoding).replace("\n", "")
            except:
                pass


class Time:
    def stop_wotch(start_time):
        tt = time.time() - start_time
        mins = tt // 60
        sec = tt % 60
        hours = mins // 60
        mins = mins % 60
        return int(hours), int(mins), int(sec)

    def trying(key, obj_time_time):
        hours, mins, sec = Time.stop_wotch(obj_time_time)
        key_len = " " * int(20 - len(key))
        print()
        print(
            "\033[A",colr().hex("#6666ff", "   Trying"),
            colr().hex("#6666ff", "["),
            colr().hex("#cc33ff", f"{key}"),
            colr().hex("#6666ff", "]"),
            colr().hex("#6666ff", "     ["),
            colr().hex("#6666ff", f"{hours}"),
            colr().hex("#6666ff", ":"),
            colr().hex("#cc33ff", f"{mins}"),
            colr().hex("#6666ff", ":"),
            colr().hex("#cc33ff", f"{sec}"),
            colr().hex("#6666ff", "]"),
            colr().hex("#6666ff", "["),
            colr().hex("#6666ff", "Ctrl+C for Kill"),
            colr().hex("#6666ff", "]"),"\033[A"
        )
        


# Hash key generater
class Hash_Generator:
    def __init__(self, str_input):
        self.hash_str = str_input

    def md5(self):
        return hashlib.md5(self.hash_str.encode("utf-8")).hexdigest()

    def sha1(self):
        return hashlib.sha1(self.hash_str.encode("utf-8")).hexdigest()

    def sha224(self):
        return hashlib.sha224(self.hash_str.encode("utf-8")).hexdigest()

    def sha256(self):
        return hashlib.sha256(self.hash_str.encode("utf-8")).hexdigest()

    def sha384(self):
        return hashlib.sha384(self.hash_str.encode("utf-8")).hexdigest()

    def sha512(self):
        return hashlib.sha512(self.hash_str.encode("utf-8")).hexdigest()

    def blake2b(self):
        return hashlib.blake2b(self.hash_str.encode("utf-8")).hexdigest()

    def blake2s(self):
        return hashlib.blake2s(self.hash_str.encode("utf-8")).hexdigest()


def result(target, key, obj_time_time):
    style = "-" * len(key)
    style2 = "-" * len(target)
    hours, mins, sec = Time.stop_wotch(obj_time_time)
    time_len = "-" * len(f"{hours}{mins}{sec}")
    if mins == "0" and sec == "0":
        Colors.blue(f"    ,-----------{time_len}---------------,")
        print(
            colr().hex("#6666ff", "    | "),
            colr().hex("#ff0000", "    Time :["),
            colr().hex("#ff8e35", "Less than a minute"),
            colr().hex("#ff0000", "]"),
            colr().hex("#6666ff", "   |"),
        )
        Colors.blue(f"    '---------------{time_len}-----------'")
    else:
        Colors.blue(f"    ,-----------{time_len}---------------,")
        print(
            colr().hex("#6666ff", "    | "),
            colr().hex("#ff0000", "    Time :["),
            colr().hex("#ff8e35", f"{hours}"),
            colr().hex("#ff0000", ":"),
            colr().hex("#ff8e35", f"{mins}"),
            colr().hex("#ff0000", ":"),
            colr().hex("#ff8e35", f"{sec}"),
            colr().hex("#ff0000", "]"),
            colr().hex("#6666ff", "   |"),
        )
        Colors.blue(f"    '---------------{time_len}-----------'")
    Colors.blue(f"    ,---------------------------------{style}{style2}----------------,")
    print(
        colr().hex("#6666ff", "    | "),
        colr().hex("#21ff00", "Password Found :"),
        colr().hex("#ff0000", "Target :"),
        colr().hex("#ff0000", "["),
        colr().hex("#ff8e35", f"{target}"),
        colr().hex("#ff0000", "]"),
        colr().hex("#ff0000", "Password :"),
        colr().hex("#ff0000", "["),
        colr().hex("#ff8e35", f"{key}"),
        colr().hex("#ff0000", "]"),
        colr().hex("#6666ff", "|"),
    )
    Colors.blue(f"    '---------------------------------{style}{style2}----------------'")


# Checking he Hashshake key
class Check_Key:
    def pdf_key(file_name_or_path, password):
        try:
            with pdfplumber.open(file_name_or_path, password=password) as pdf:
                return True
        except pdfplumber.pdfminer.pdfdocument.PDFPasswordIncorrect:
            return False

    def rar_key(file_name_or_path, password):
        f = RarFile(file_name_or_path)
        d = f.namelist()
        try:
            f.read(d[0], pwd=str(password).encode())
            f.close()
            return True
        except:
            f.close()
            return False

    def zip_key(file_name_or_path, password):
        f = zipfile.ZipFile(file_name_or_path)
        d = f.filelist[0]
        try:
            f.read(d.filename, pwd=str(password).encode())
            f.close()
            return True
        except:
            f.close()
            return False

    def ms_office_key(world_excel_powerpoint_rb_file_object, password):
        ms_f = msoffcrypto.OfficeFile(world_excel_powerpoint_rb_file_object)
        ms_f.load_key(password=str(password))
        try:
            ms_f.decrypt(io.BytesIO())
            return True
        except msoffcrypto.exceptions.InvalidKeyError:
            return False

    def hash_key(_hash, key, num):
        hash_g = Hash_Generator(key)
        if num == "1":
            if hash_g.md5() == _hash:
                return True
            else:
                return False
        elif num == "2":
            if hash_g.sha1() == _hash:
                return True
            else:
                return False
        elif num == "3":
            if hash_g.sha224() == _hash:
                return True
            else:
                return False
        elif num == "4":
            if hash_g.sha256() == _hash:
                return True
            else:
                return False
        elif num == "5":
            if hash_g.sha384() == _hash:
                return True
            else:
                return False
        elif num == "6":
            if hash_g.sha512() == _hash:
                return True
            else:
                return False
        elif num == "7":
            if hash_g.blake2b() == _hash:
                return True
            else:
                return False
        elif num == "8":
            if hash_g.blake2s() == _hash:
                return True
            else:
                return False


def sub_menu():
    print(
        colr().hex("#6666ff", "\n    Select"),
        colr().hex("#ff0000", "[1]"),
        colr().hex("#6666ff", "PDF"),
        colr().hex("#ff0000", " [2]"),
        colr().hex("#6666ff", "RAR"),
        colr().hex("#ff0000", "[3]"),
        colr().hex("#6666ff", "ZIP"),
        colr().hex("#ff0000", "[4]"),
        colr().hex("#6666ff", "MS_Office"),
    )
    print(
        colr().hex("#ff0000", "           [5]"),
        colr().hex("#6666ff", "Hash"),
        colr().hex("#ff0000", "[6]"),
        colr().hex("#6666ff", "Generate Dictionay"),
        colr().hex("#ff0000", "[0]"),
        colr().hex("#6666ff", "Exit"),
    )


# =================================================================================================================================================================================================================================== #

# Brute force attack


def brute_force():
    sub_menu()
    sleep(0.5)
    choice = input(colr().hex("#ff0000", "\n    Brute Force/# "))
    if choice == "1":

        def pdf_crack():
            try:
                pdf = (
                    input(
                        colr().hex(
                            "#6666ff",
                            f"\n    Input PDF File name or path >> ",
                            rgb_mode=True,
                        )
                    )
                    .replace("'", "")
                    .replace('"', "")
                    .lstrip()
                    .rstrip()
                )
                Colors.red(
                    "\n    EG: abcdefghijklmnopqrstuvwz or ABCDEFGHIKLMNOPQRSTUVWZ or 1234567890 "
                )
                character_list = input(
                    colr().hex("#6666ff", "    Characters >> ")
                ).replace(" ", "")
                minimum = int(
                    input(colr().hex("#6666ff", "    Input Min Length Password >> "))
                )
                maximum = int(
                    input(colr().hex("#6666ff", "    Input Max Length Password >> "))
                )
                # show the user input to verification
                Colors.dark_rose("\n    ******* YOUR INPUT RESULt *******\n")
                print(
                    colr().hex("#ff0000", "         PDF Name :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{pdf}",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "\n         Character :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{character_list}",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "\n         Minimum Length :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{minimum}",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "\n         Maximum Length :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{maximum}",
                        rgb_mode=True,
                    ),
                )
                Colors.dark_green("\n    Check the input is correct ? \n")
                answer = input(colr().hex("#6666ff", "    y or n or e = exit > "))
                print("")
                answer = answer.lower()
                if answer == "y" or answer == "yes":
                    start_time = time.time()
                    for i in Generate.BrutForce(character_list, minimum, maximum):
                        Time.trying(i, start_time)
                        if Check_Key.pdf_key(pdf, i) == True:
                            result(pdf, i, start_time)
                            break
                        else:
                            pass
                    input(colr().hex("#ff0000", f"\n\n    Press enter to  main # "))
                    main_banner()
                elif answer == "n" or answer == "no":
                    pdf_crack()
                elif answer == "e" or answer == "exit":
                    Colors.red("\n Exit")
                    exit()
                else:
                    Operators.case_default()

            except ValueError:
                Operators.case_default()

        pdf_crack()
    elif choice == "2":

        def rar_crack():
            try:
                rar = (
                    input(
                        colr().hex(
                            "#6666ff",
                            f"\n    Input RAR File name or path >> ",
                            rgb_mode=True,
                        )
                    )
                    .replace("'", "")
                    .replace('"', "")
                    .lstrip()
                    .rstrip()
                )

                Colors.red(
                    "\n    EG: abcdefghijklmnopqrstuvwz or ABCDEFGHIKLMNOPQRSTUVWZ or 1234567890 "
                )
                character_list = input(
                    colr().hex("#6666ff", " Characters >> ")
                ).replace(" ", "")
                minimum = int(
                    input(colr().hex("#6666ff", "    Input Min Length Password >> "))
                )
                maximum = int(
                    input(colr().hex("#6666ff", "    Input Max Length Password >> "))
                )
                # show the user input to verification
                Colors.dark_rose("\n      ******* YOUR INPUT RESULt *******\n")
                print(
                    colr().hex("#ff0000", "    RAR Name :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{rar}",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "\n        Character :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{character_list}",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "\n        Minimum Length :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{minimum}",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "\n        Maximum Length :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{maximum}",
                        rgb_mode=True,
                    ),
                )
                Colors.blue("\n    Check the input is correct ? \n")
                answer = input(colr().hex("#6666ff", "    y or n or e = exit > "))
                answer = answer.lower()
                if answer == "y" or answer == "yes":
                    start_time = time.time()
                    for i in Generate.BrutForce(character_list, minimum, maximum):
                        Time.trying(i, start_time)
                        if Check_Key.rar_key(rar, i) == True:
                            result(rar, i, start_time)
                            break
                        else:
                            pass
                    input(colr().hex("#ff0000", f"\n\n    Press enter to  main # "))
                    main_banner()
                elif answer == "n" or answer == "no":
                    rar_crack()
                elif answer == "e" or answer == "exit":
                    Colors.red("\n Exit")
                    exit()
                else:
                    Operators.case_default()

            except ValueError:
                Operators.case_default()

        rar_crack()

    elif choice == "3":

        def zip_crack():
            try:
                zip = (
                    input(
                        colr().hex(
                            "#6666ff",
                            f"\n    Input ZIP File name or path >> ",
                            rgb_mode=True,
                        )
                    )
                    .replace("'", "")
                    .replace('"', "")
                    .lstrip()
                    .rstrip()
                )
                Colors.red(
                    "\n    EG: abcdefghijklmnopqrstuvwz or ABCDEFGHIKLMNOPQRSTUVWZ or 1234567890 "
                )
                character_list = input(
                    colr().hex("#6666ff", "    Characters >> ")
                ).replace(" ", "")
                minimum = int(
                    input(colr().hex("#6666ff", "    Input Min Length Password >> "))
                )
                maximum = int(
                    input(colr().hex("#6666ff", "    Input Max Length Password >> "))
                )
                # show the user input to verification
                Colors.dark_rose("\n    ******* YOUR INPUT RESULt *******\n")
                print(
                    colr().hex("#ff0000", "         ZIP Name :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{zip}",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "\n         Character :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{character_list}",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "\n         Minimum Length :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{minimum}",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "\n         Maximum Length :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{maximum}",
                        rgb_mode=True,
                    ),
                )
                Colors.dark_green("\n    Check the input is correct ? \n")
                answer = input(colr().hex("#6666ff", "    y or n or e = exit > "))
                print("")
                answer = answer.lower()
                if answer == "y" or answer == "yes":
                    start_time = time.time()
                    for i in Generate.BrutForce(character_list, minimum, maximum):
                        Time.trying(i, start_time)
                        if Check_Key.zip_key(zip, str(i)) == True:
                            result(zip, i, start_time)
                            break
                        else:
                            pass
                    input(colr().hex("#ff0000", f"\n\n    Press enter to  main # "))
                    main_banner()
                elif answer == "n" or answer == "no":
                    zip_crack()
                elif answer == "e" or answer == "exit":
                    Colors.red("\n    Exit")
                    exit()
                else:
                    Operators.case_default()

            except ValueError:
                Operators.case_default()

        zip_crack()

    elif choice == "4":

        def e_w_p():
            try:
                ms_f = (
                    input("\n    Input (Excel,World,PowerPoint) File name or path >> ")
                    .replace("'", "")
                    .replace('"', "")
                    .lstrip()
                    .rstrip()
                )

                Colors.red(
                    "\n    EG: abcdefghijklmnopqrstuvwz or ABCDEFGHIKLMNOPQRSTUVWZ or 1234567890 "
                )
                character_list = input(
                    colr().hex("#6666ff", "    Characters >> ")
                ).replace(" ", "")
                minimum = int(
                    input(colr().hex("#6666ff", "    Input Min Length Password >> "))
                )
                maximum = int(
                    input(colr().hex("#6666ff", "    Input Max Length Password >> "))
                )
                # show the user input to verification
                Colors.dark_rose("\n    ******* YOUR INPUT RESULt *******\n")
                print(
                    colr().hex(
                        "#ff0000", "    Excel,World,PowerPoint Name :", rgb_mode=True
                    ),
                    colr().hex(
                        "#00ff8d",
                        f"{ms_f}",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "    Character :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{character_list}",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "    Minimum Length :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{minimum}",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "    Maximum Length :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{maximum}",
                        rgb_mode=True,
                    ),
                )
                Colors.blue("\n    Check the input is correct ? \n")
                answer = input(colr().hex("#6666ff", "    y or n or e = exit > "))
                answer = answer.lower()
                if answer == "y" or answer == "yes":
                    m = open(ms_f, "rb")
                    start_time = time.time()
                    for i in Generate.BrutForce(character_list, minimum, maximum):
                        Time.trying(i, start_time)
                        if Check_Key.ms_office_key(m, str(i)) == True:
                            m.close()
                            result(ms_f, i, start_time)
                            break
                        else:
                            pass
                    m.close()
                    input(colr().hex("#ff0000", f"\n\n    Press enter to  main # "))
                    main_banner()
                elif answer == "n" or answer == "no":
                    e_w_p()
                elif answer == "e" or answer == "exit":
                    Colors.red("\n Exit")
                    exit()
                else:
                    Operators.case_default()

            except ValueError:
                Operators.case_default()

        e_w_p()

    elif choice == "5":

        def hash_g():
            try:
                hash = (
                    input("\n    Input Encripted Hash String >> ")
                    .replace("'", "")
                    .replace('"', "")
                    .lstrip()
                    .rstrip()
                )
                hash_type = input(
                    f"Select [1]MD5 [2]SHA1 [3]SHA224 [4]SHA256 [5]SHA384 [6]SHA512 [7]BLAKE2B [8]BLAKE2S Type >> "
                )

                Colors.red(
                    "\n    EG: abcdefghijklmnopqrstuvwz or ABCDEFGHIKLMNOPQRSTUVWZ or 1234567890 "
                )
                character_list = input(
                    colr().hex("#6666ff", "    Characters >> ")
                ).replace(" ", "")
                minimum = int(
                    input(colr().hex("#6666ff", "Input Min Length Password >> "))
                )
                maximum = int(
                    input(colr().hex("#6666ff", "Input Max Length Password >> "))
                )
                # show the user input to verification
                Colors.dark_rose("\n      ******* YOUR INPUT RESULt *******\n")
                print(
                    colr().hex(
                        "#ff0000", "        Encripted Hash String :", rgb_mode=True
                    ),
                    colr().hex(
                        "#00ff8d",
                        f"{hash}",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "\n        Hash Type :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{hash_type}",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "\n        Character :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{character_list}",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "\n        Minimum Length :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{minimum}",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "\n        Maximum Length :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{maximum}",
                        rgb_mode=True,
                    ),
                )
                Colors.blue("\n    Check the input is correct ? \n")
                answer = input(colr().hex("#6666ff", "    y or n or e = exit > "))
                answer = answer.lower()
                if answer == "y" or answer == "yes":
                    start_time = time.time()
                    for i in Generate.BrutForce(character_list, minimum, maximum):
                        Time.trying(i, start_time)
                        if Check_Key.hash_key(hash, str(i), hash_type) == True:
                            result(hash, i, start_time)
                            break
                        else:
                            pass
                    input(colr().hex("#ff0000", f"\n\n    Press enter to  main # "))
                    main_banner()
                elif answer == "n" or answer == "no":
                    hash_g()
                elif answer == "e" or answer == "exit":
                    Colors.red("\n Exit")
                    exit()
                else:
                    Operators.case_default()

            except ValueError:
                Operators.case_default()

        hash_g()

    elif choice == "6":

        def generate_dicitory():
            try:
                path = (
                    input(colr().hex("#6666ff", "\n    Input File name or path >> "))
                    .replace("'", "")
                    .replace('"', "")
                    .lstrip()
                    .rstrip()
                )
                Colors.red(
                    "\n    EG: abcdefghijklmnopqrstuvwz or ABCDEFGHIKLMNOPQRSTUVWZ or 1234567890 "
                )
                character_list = input(
                    colr().hex("#6666ff", " Characters   >> ")
                ).replace(" ", "")
                minimum = int(
                    input(colr().hex("#6666ff", "    Input Min Length Password >> "))
                )
                maximum = int(
                    input(colr().hex("#6666ff", "    Input Max Length Password >> "))
                )
                # show the user input to verification
                Colors.dark_rose("\n      ******* YOUR INPUT RESULt *******\n")
                print(
                    colr().hex("#ff0000", "        Path :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{path}",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "\n        Character :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{character_list}",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "\n        Minimum Length :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{minimum}",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "\n        Maximum Length :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{maximum}",
                        rgb_mode=True,
                    ),
                )
                Colors.blue("\n    Check the input is correct ? \n")
                answer = input(colr().hex("#6666ff", "    y or n or e = exit > "))
                answer = answer.lower()
                if answer == "y" or answer == "yes":
                    start_time = time.time()
                    b_list = open(path, "w")
                    th = threading.Thread(target=main_banner.dic_gen_show)

                    th.start()
                    for i in Generate.BrutForce(character_list, minimum, maximum):
                        b_list.write(str(i) + "\n")
                        b_list.close()

                    time.sleep(2)
                    result(
                        character_list, path, start_time
                    )  # put directory result function calling
                    input(colr().hex("#ff0000", f"\n\n    Press enter to  main # "))
                    main_banner()
                elif answer == "n" or answer == "no":
                    generate_dicitory()
                elif answer == "e" or answer == "exit":
                    Colors.red("\n Exit")
                    exit()
                else:
                    Operators.case_default()

            except ValueError:
                Operators.case_default()

        generate_dicitory()


# =================================================================================================================================================================================================================================== #


# =================================================================================================================================================================================================================================== #

# Directory Attack


def directory():
    sub_menu()
    sleep(0.5)

    choice = input(colr().hex("#ff0000", "\n    Directory/# "))
    if choice == "1":

        def pdf_directory():
            try:
                pdf = (
                    input(
                        colr().hex(
                            "#6666ff",
                            f"\n    Input PDF File name or path >> ",
                            rgb_mode=True,
                        )
                    )
                    .replace("'", "")
                    .replace('"', "")
                    .lstrip()
                    .rstrip()
                )

                dir_path = input(
                    colr().hex("#6666ff", "    Input Directory File Path or Name >> ")
                )
                # show the user input to verification
                Colors.dark_rose("\n    ******* YOUR INPUT RESULt *******\n")
                print(
                    colr().hex("#ff0000", "         PDF Name :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{pdf}",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "\n         Directory Name:", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{dir_path}",
                        rgb_mode=True,
                    ),
                )
                Colors.dark_green("\n    Check the input is correct ? \n")
                answer = input(colr().hex("#6666ff", "    y or n or e = exit > "))
                answer = answer.lower()
                if answer == "y" or answer == "yes":
                    start_time = time.time()
                    for i in Generate.directory(dir_path):
                        Time.trying(i, start_time)
                        if Check_Key.pdf_key(pdf, i) == True:
                            result(pdf, i, start_time)
                            break
                        else:
                            pass
                    input(colr().hex("#ff0000", f"\n\n    Press enter to  main # "))
                    main_banner()
                elif answer == "n" or answer == "no":
                    pdf_directory()
                elif answer == "e" or answer == "exit":
                    Colors.red("\n Exit")
                    exit()
                else:
                    Operators.case_default()

            except ValueError:
                Operators.case_default()

        pdf_directory()

    elif choice == "2":

        def rar_directory():
            try:
                rar = (
                    input(
                        colr().hex(
                            "#6666ff",
                            f"\n    Input RAR File name or path >> ",
                            rgb_mode=True,
                        )
                    )
                    .replace("'", "")
                    .replace('"', "")
                    .lstrip()
                    .rstrip()
                )

                dir_path = input(
                    colr().hex("#6666ff", "    Input Directory File Path or Name >> ")
                )
                # show the user input to verification
                Colors.dark_rose("\n    ******* YOUR INPUT RESULt *******\n")
                print(
                    colr().hex("#ff0000", "         RAR Name :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{rar}",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "\n         Directory Name:", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{dir_path}",
                        rgb_mode=True,
                    ),
                )
                Colors.dark_green("\n    Check the input is correct ? \n")
                answer = input(colr().hex("#6666ff", "    y or n or e = exit > "))
                answer = answer.lower()
                if answer == "y" or answer == "yes":
                    start_time = time.time()
                    for i in Generate.directory(dir_path):
                        Time.trying(i, start_time)
                        if Check_Key.rar_key(rar, i) == True:
                            result(rar, i, start_time)
                            break
                        else:
                            pass
                    input(colr().hex("#ff0000", f"\n\n    Press enter to  main # "))
                    main_banner()
                elif answer == "n" or answer == "no":
                    rar_directory()
                elif answer == "e" or answer == "exit":
                    Colors.red("\n Exit")
                    exit()
                else:
                    Operators.case_default()

            except ValueError:
                Operators.case_default()

        rar_directory()
    elif choice == "3":

        def zip_directory():
            try:
                zip = (
                    input(
                        colr().hex(
                            "#6666ff",
                            f"\n    Input ZIP File name or path >> ",
                            rgb_mode=True,
                        )
                    )
                    .replace("'", "")
                    .replace('"', "")
                    .lstrip()
                    .rstrip()
                )

                dir_path = input(
                    colr().hex("#6666ff", "    Input Directory File Path or Name >> ")
                )
                # show the user input to verification
                Colors.dark_rose("\n    ******* YOUR INPUT RESULt *******\n")
                print(
                    colr().hex("#ff0000", "         ZIP Name :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{zip}",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "\n         Directory Name:", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{dir_path}",
                        rgb_mode=True,
                    ),
                )
                Colors.dark_green("\n    Check the input is correct ? \n")
                answer = input(colr().hex("#6666ff", "    y or n or e = exit > "))
                answer = answer.lower()
                if answer == "y" or answer == "yes":
                    start_time = time.time()
                    for i in Generate.directory(dir_path):
                        Time.trying(i, start_time)
                        if Check_Key.zip_key(zip, str(i)) == True:
                            result(zip, i, start_time)
                            break
                        else:
                            pass
                    input(colr().hex("#ff0000", f"\n\n    Press enter to  main # "))
                    main_banner()
                elif answer == "n" or answer == "no":
                    zip_directory()
                elif answer == "e" or answer == "exit":
                    Colors.red("\n Exit")
                    exit()
                else:
                    Operators.case_default()

            except ValueError:
                Operators.case_default()

        zip_directory()
    elif choice == "4":

        def e_w_p_directory():
            try:
                e_w_p = (
                    input(
                        colr().hex(
                            "#6666ff",
                            f"\n    Input Pdf File name or path >> ",
                            rgb_mode=True,
                        )
                    )
                    .replace("'", "")
                    .replace('"', "")
                    .lstrip()
                    .rstrip()
                )

                dir_path = input(
                    colr().hex("#6666ff", "    Input Directory File Path or Name >> ")
                )
                # show the user input to verification
                Colors.dark_rose("\n    ******* YOUR INPUT RESULt *******\n")
                print(
                    colr().hex("#ff0000", "         PDF Name :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{e_w_p}",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "\n         Directory Name:", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{dir_path}",
                        rgb_mode=True,
                    ),
                )
                Colors.dark_green("\n    Check the input is correct ? \n")
                answer = input(colr().hex("#6666ff", "    y or n or e = exit > "))
                answer = answer.lower()
                if answer == "y" or answer == "yes":
                    open_e_w_p_file = open(e_w_p, "rb")
                    start_time = time.time()
                    for i in Generate.directory(dir_path):
                        Time.trying(i, start_time)
                        if Check_Key.ms_office_key(open_e_w_p_file, str(i)) == True:
                            result(e_w_p, i, start_time)
                            break
                        else:
                            pass
                    input(colr().hex("#ff0000", f"\n\n    Press enter to  main # "))
                    main_banner()
                elif answer == "n" or answer == "no":
                    e_w_p_directory()
                elif answer == "e" or answer == "exit":
                    Colors.red("\n Exit")
                    exit()
                else:
                    Operators.case_default()

            except ValueError:
                Operators.case_default()

        e_w_p_directory()
    elif choice == "5":

        def hash_directory():
            try:
                hash = (
                    input("\n    Input Encripted Hash String >> ")
                    .replace("'", "")
                    .replace('"', "")
                    .lstrip()
                    .rstrip()
                )
                hash_type = input(
                    f"Select [1]MD5 [2]SHA1 [3]SHA224 [4]SHA256 [5]SHA384 [6]SHA512 [7]BLAKE2B [8]BLAKE2S Type >> "
                )
                dir_path = input(
                    colr().hex("#6666ff", "    Directory Name or Path >> ")
                ).replace(" ", "")
                # show the user input to verification
                Colors.dark_rose("\n      ******* YOUR INPUT RESULt *******\n")
                print(
                    colr().hex(
                        "#ff0000", "        Encripted Hash String :", rgb_mode=True
                    ),
                    colr().hex(
                        "#00ff8d",
                        f"{hash}",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "\n        Hash Type :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{hash_type}",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "\n        Directory Name :", rgb_mode=True),
                    colr().hex(
                        "#00ff8d",
                        f"{dir_path}",
                        rgb_mode=True,
                    ),
                )
                Colors.dark_green("\n    Check the input is correct ? \n")
                answer = input(colr().hex("#6666ff", "    y or n or e = exit > "))
                answer = answer.lower()
                if answer == "y" or answer == "yes":
                    start_time = time.time()
                    for i in Generate.directory(dir_path):
                        Time.trying(i, start_time)
                        if Check_Key.hash_key(hash, i, hash_type) == True:
                            result(hash, i, start_time)
                            break
                        else:
                            pass
                    input(colr().hex("#ff0000", f"\n\n    Press enter to  main # "))
                    main_banner()
                elif answer == "n" or answer == "no":
                    hash_directory()
                elif answer == "e" or answer == "exit":
                    Colors.red("\n Exit")
                    exit()
                else:
                    Operators.case_default()

            except ValueError:
                Operators.case_default()

        hash_directory()
    else:
        Operators.case_default()


def main_banner():
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

    Colors.blue("\n      " + dash)
    null = ""
    dash = null.center(58, "-")
    Colors.blue("\n                   ," + dash + ",")
    # Main Choice
    print(
        colr().hex("#0000ff", "                   |"),
        colr().hex("#6666ff", "Select"),
        colr().hex("#ff0000", "[1]"),
        colr().hex("#6666ff", "BruteForce"),
        colr().hex("#ff0000", " [2]"),
        colr().hex("#6666ff", "Directory"),
        colr().hex("#ff0000", "[3]"),
        colr().hex("#6666ff", "Random"),
        colr().hex("#ff0000", "[0]"),
        colr().hex("#6666ff", "Exit"),
        colr().hex("#0000ff", "|"),
    )
    Colors.blue("                   '" + dash + "'")
    sleep(0.5)
    # Main choice
    try:
        choice = input(colr().hex("#ff0000", "\n    Cracker/# "))
        if choice == "1":
            brute_force()
        elif choice == "2":
            directory()
        elif choice == "3":
            print("3")

        elif choice == "0":
            Operators.exit()
        else:
            print("")
            Operators.case_default()

    except KeyboardInterrupt:
        Colors.red("\n\n______KeyboardInterrupted_____")


# Call choice function
main_banner()
