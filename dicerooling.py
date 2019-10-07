""" @ Author:- Ritik Kumar"""

import random
repeat = True
while repeat:
    print("you got",random.randint(1,6))
    print("do you want to rolled again y/n")
    repeat = "y" in input()
