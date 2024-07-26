import os
import subprocess
while True:
    print("Which one Do You Want to Choose?")
    print("1) Easy Mode")
    print("2) Advanced Mode")
    choise = input()
    if choise == "1":
        subprocess.run(["python", "ez-mode.py"])
        break
    elif choise == "2":
        os.system("advanced-mode.py")
        break
    else:
        print("Wrong Value")