import sys 
import pyfiglet as pyg  
input_str = input("Input : ")
if sys.argv[1] == '-f' or sys.argv[1] == '--font':
    res = pyg.figlet_format(input_str,font=sys.argv[2])
else:
    res = pyg.figlet_format(input_str)
print(res)