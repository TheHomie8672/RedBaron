# Library of Tools
from Calculator_v1 import calculator
from NumSort_v1 import sort2
from NumberGuess_PyTools import LVL_1
from SciNoteConv import scientific_to_standard
from Number_Extrapolating_Algorithm import *
from Quadratics_calc import *
from wifi_password_extractor_v1 import *
def library():
        while True:
            
        
            
            help = print("calculator (calc), Number Sorter (sort), NumberGuess(NumGuess), Scientific to Standard(SciCon)")
            help2 = print("Extrapolation Algorithm(NumSeq), quadratics calculator(quadratics), Wifi Password Extractor(wifi)")
            command = input("Please select a tool by typing its corresponding name: YOU:  ")
            instructions = print("To select a program, please type the command name into the input, for a list of commands please type help or help2")
        
            if command.lower() == "help":
                help
            if command.lower() == "help2":
                help2
            if command.lower() == "exit":
                print("Goodbye")
                break
            
            
            if command.lower() == "calc":
                calculator()
            if command.lower() == "sort":
                sort2()
            if command.lower() == "help":
                help()
            if command.lower() == "numguess":
                LVL_1()
            if command.lower() == "scicon":
                scientific_to_standard()
            if command.lower() == "numseq":
                Num_Extrapolator_Algorith()
            if command.lower() == "quadratics":
                quadratics_calc()
            if command.lower() == "wifi":
                wifi_passwords()
                
               
if ValueError:
    library()
library()  