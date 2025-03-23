#solution01
# my_string = input()
# if len(my_string)<=2:
#     print("")
# else:
#     print(my_string[:2] + my_string[-2:])
from problemsloving.SU_Python_QZ1 import my_str, new_str

#solution02
my_str = input()
if len(my_str) != 0:
    print(my_str[0] + '@'*(len(my_str)-1))
else:
    print("")

