import sys
import os
from compute import *
# Vigneswar Mourouguessin - 40057918


class Class_grade :
    
        A1 = []
        A2 = []
        Project = []
        Test1 = []
        Test2 = []
        dict_file = {}
    
        def function(self):
            print("welcome")
        
        def __init__(self):
            # Files to be placed in this path : print(os.getcwd())
            self.A1 = open('a1.txt').read().split("\n")
            self.A2 = open('a2.txt').read().split("\n")
            self.Project = open('project.txt').read().split("\n")
            self.Test1 = open('test1.txt').read().split("\n")
            self.Test2 = open('test2.txt').read().split("\n")
            
            with open("class.txt") as f:
                for line in f:
                   (key, val1, val2) = line.split("|")
                   self.dict_file[int(key)] = val2[:-1] + "," + val1
            
        def welcome(self, G, C):
            print("")
            print("1> Display individual component")
            print("2> Display component average")
            print("3> Display Standard Report")
            print("4> Sort by alternate column")
            print("5> Change Pass/Fail point")
            print("6> Exit")
            user_input = int(input("\nselect your option in numbers (1-6) :\n"))
                       
            if (user_input <= 0) or (user_input > 6)  :
                user_input = int(input("Wrong option - select option between (1-6) :"))
            else:    
                C.task(user_input, G, C)
            print("\n*** End of task ***")
            G.welcome(G, C)
            #check = int(input("\nDo You Wish to Continue 1-Yes  2-No, Enter 1 or 2:\n"))
            #if(check == 1):
                #G.welcome(G, C)
                #print()
            #else :
            #    C.task(6, G, C)
        
        if __name__ == "__main__":
            
            print("Welcome")
            
            C = Class_compute()    
            G = Class_grade()
            obj = Class_grade()
            
            C.checking(G, C)
            
            obj.welcome(G, C)
            
