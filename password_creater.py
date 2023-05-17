import random
import string
import os


class Alphanumeric:
    def generate_password_8(length , maxlength):
        for i in range(length , maxlength + 1):
            characters = string.ascii_letters + string.digits
            password = "".join(random.choice(characters) for _ in range(i))
            print (password)
            

    


# num_passwords = int(
#     input("Enter you Password count : ")
# )  # Number of passwords to generate
# password_file = input("Enter your file name : ")


def creater():
    i = 1
    print(" Password is creating ......")
    for i in range(num_passwords):
        print(i)
        password_8 = Alphanumeric.generate_password_8()
        password_9 = Alphanumeric.generate_password_9()
        password_10 = Alphanumeric.generate_password_10()
        password_11 = Alphanumeric.generate_password_11()
        password_12 = Alphanumeric.generate_password_12()
        password_13 = Alphanumeric.generate_password_13()
        password_14 = Alphanumeric.generate_password_14()
        password_15 = Alphanumeric.generate_password_15()
        password_16 = Alphanumeric.generate_password_16()
        password_17 = Alphanumeric.generate_password_17()
        password_18 = Alphanumeric.generate_password_18()
        password_19 = Alphanumeric.generate_password_19()
        password_20 = Alphanumeric.generate_password_20()
        print(password_8)
        print(password_9)
        print(password_10)
        print(password_11)
        print(password_12)
        print(password_13)
        print(password_14)
        print(password_15)
        print(password_16)
        print(password_17)
        print(password_18)
        print(password_19)
        print(password_20)

        os.system(f"\n echo {password_8} >> {password_file}")
        os.system(f"echo {password_9} >> {password_file}")
        os.system(f"echo {password_10} >> {password_file}")
        os.system(f"echo {password_11} >> {password_file}")
        os.system(f"echo {password_12} >> {password_file}")
        os.system(f"echo {password_13} >> {password_file}")
        os.system(f"echo {password_14} >> {password_file}")
        os.system(f"echo {password_15} >> {password_file}")
        os.system(f"echo {password_16} >> {password_file}")
        os.system(f"echo {password_17} >> {password_file}")
        os.system(f"echo {password_18} >> {password_file}")
        os.system(f"echo {password_19} >> {password_file}")
        os.system(f"echo {password_20} >> {password_file}")
    print(" Password successfully finished")
Alphanumeric.generate_password_8(3 ,5)
