import sysconfig
import os
import sys
import operator
from grades import *

# Vigneswar Mourouguessin - 40057918


class Class_compute:
    
    dict_file_a1 = {}
    dict_file_a2 = {}
    dict_file_pr = {}
    dict_file_t1 = {}
    dict_file_t2 = {} 
    final_dict = {} 
    final_list = []
    dict = {}
    
    def function(self):
        print()
        
    def __init__(self):
        print()
            
    def checking(self, G, C):
        self.dict_file_a1 = C.generate(G, C, G.A1)
        self.dict_file_a2 = C.generate(G, C, G.A2)
        self.dict_file_pr = C.generate(G, C, G.Project)
        self.dict_file_t1 = C.generate(G, C, G.Test1)
        self.dict_file_t2 = C.generate(G, C, G.Test2)
        self.dict = {}
        self.final_dict = {} 
        self.final_list = []
        
        option = 50
        for id in G.dict_file.keys():
            C.getgrade(id, G, C, option)
        
        # print(dict_file_a1)
        # print(dict_file_a2)
        # print(dict_file_pr)
        # print(dict_file_t1)
        # print(dict_file_t2)
    
    def generate(self, G, C, mylist=[]):
        dict_file_new = {}       
        for id in G.dict_file.keys():
                for x in mylist[1:]:
                    temp = x.split("|")
                    if(int(temp[0]) == id):
                        sid = id
                        name = G.dict_file[id]
                        mark = temp[1]
                        dict_file_new[int(sid)] = name + "," + mark
        return dict_file_new
    
    def task(self, taskId, G, C):
        task = taskId
        
        if(task == 1):
            C.Display_individual_component(G, C)
        elif(task == 2):
            C.Display_component_average(G, C)
        elif(task == 3):
            C.Display_Standard_Report(G, C)
        elif(task == 4):
            C.Sort_alternate_column(G, C)
        elif(task == 5):
            C.Change_point(G, C)
        else :
            C.Exit()
        
     # task 1 to print individual component   
    def Display_individual_component(self, G, C):
        C.get_input(G, C)
                
    def get_input(self, G, C):
        user_input = input("Choose the component name (A1, A2, PR, T1, or T2) :\n")
        if(user_input == "A1") or (user_input == "a1"):
            print("\nA1" + "  grades  " + G.A1[0])
            C.call_print(G, C, G.A1)
        elif(user_input == "A2") or (user_input == "a2"):
            print("\nA2" + "  grades  " + G.A2[0])
            C.call_print(G, C, G.A2)
        elif(user_input == "PR") or (user_input == "pr"):
            print("\nProject" + "  grades  " + G.Project[0])
            C.call_print(G, C, G.Project)
        elif(user_input == "T1") or (user_input == "t1"):
            print("\nTest1" + "  grades  " + G.Test1[0])
            C.call_print(G, C, G.Test1)
        elif(user_input == "T2") or (user_input == "t2"):
            print("\nTest2" + "  grades  " + G.Test2[0])
            C.call_print(G, C, G.Test2)
        else:
            print("Invalid input enter from choice (A1, A2, PR, T1, or T2) :\n")
            C.get_input(G, C)
    
    def call_print(self, G, C, mylist=[]):
        dict_file_new = {}       
        for id in G.dict_file.keys():
                for x in mylist[1:]:
                    temp = x.split("|")
                    if(int(temp[0]) == id):
                        sid = id
                        name = G.dict_file[id]
                        mark = temp[1]
                        # print(sid, '\t', name, '\t','\t', mark)
                        print("%-10s %-20s %-10s" % (sid, name, mark))
                        dict_file_new[int(sid)] = name + "," + mark
         
    # task 2  
    def Display_component_average(self, G, C):
        C.get_input_avg(G, C)
        
    def get_input_avg(self, G, C):
        user_input = input("Choose the component name (A1, A2, PR, T1, or T2) :\n")
        if(user_input == "A1") or (user_input == "a1"):
            print("\nA1 average", C.getavg(G.A1), "/", G.A1[0])
        elif(user_input == "A2") or (user_input == "a2"):
            print("\nA2 average", C.getavg(G.A2), "/", G.A2[0])
        elif(user_input == "PR") or (user_input == "pr"):
            print("\nProject average", C.getavg(G.Project), "/", G.Project[0])
        elif(user_input == "T1") or (user_input == "t1"):
            print("\nT1 average", C.getavg(G.Test1), "/", G.Test1[0])
        elif(user_input == "T2") or (user_input == "t2"):
            print("\nT2 average", C.getavg(G.Test2), "/", G.Test2[0])
        else:
            print("Invalid input enter from choice (A1, A2, PR, T1, or T2) :\n")
            C.get_input_avg(G, C)
    
    def getavg(self, temp=[]):
        sum = 0
        count = 0
        for x in temp[1:]:
            count = count + 1
            number = x.split("|")
            # print(number)
            if(number[1] == ' '):
                number[1] = 0
            sum = int(number[1]) + sum
            avg = sum / int(count)
        return round(avg, 2)
    
    # Task 3 
    def Display_Standard_Report(self, G, C):
               
        # print(G.dict_file)
        # print(C.dict_file_a1)
        # print(C.dict_file_a2)
        # print(C.dict_file_pr)
        # print(C.dict_file_t1)
        # print(C.dict_file_t2)
        option = 50
        
        print("Pass/ Fail point :", option)
        
        for id in G.dict_file.keys():
            C.getgrade(id, G, C, option)
            
        C.printGrade()   
        self.final_list = [] 
        # print(C.final_dict)
        
    def printGrade(self):
        print("%-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s" % ("ID", "LN" , "FN", "A1", "A2", "PR", "T1", "T2", "GR", "FL"))
        
        for val in sorted(self.final_dict.keys()):
            (id, lname, fname, a1_mks, a2_mks, pr_mks, t1_mks, t2_mks, grade, band) = self.final_dict[val]
            if(a1_mks == 'zero'): 
                a1_mks = ' '
            if(a2_mks == 'zero'): 
                a2_mks = ' '
            if(pr_mks == 'zero'): 
                pr_mks = ' '
            if(t1_mks == 'zero'): 
                t1_mks = ' '
            if(t2_mks == 'zero'): 
                t2_mks = ' '
            
            print("%-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s" % (id, lname, fname, a1_mks, a2_mks, pr_mks, t1_mks, t2_mks, grade, band))
        
    def getgrade(self, id, G, C, option):
        Id = id
        grade = 0
        A1_mks = 0
        A2_mks = 0
        T1_mks = 0
        T2_mks = 0
        Pr_mks = 0
        name = C.get_name(id, G, C, G.dict_file)
        lname = name[0]
        fname = name[1]
        a1_mks = C.getmarks(id, G, C, C.dict_file_a1)
        a2_mks = C.getmarks(id, G, C, C.dict_file_a2)
        pr_mks = C.getmarks(id, G, C, C.dict_file_pr)
        t1_mks = C.getmarks(id, G, C, C.dict_file_t1)
        t2_mks = C.getmarks(id, G, C, C.dict_file_t2)
        
        if(a1_mks == 'zero'):
            A1_mks = 0   
        else:
            A1_mks = int(a1_mks)
            
        if(a2_mks == 'zero'):
            A2_mks = 0
        else:
            A2_mks = int(a2_mks)
        
        if(pr_mks == 'zero'):
            PR_mks = 0
        else:
            PR_mks = int(pr_mks)
        
        if(t1_mks == 'zero'):
            T1_mks = 0
        else:
            T1_mks = int(t1_mks)
        
        if(t2_mks == 'zero'):
            T2_mks = 0
        else:
            T2_mks = int(t2_mks)     
        # print(lname, fname, a1_mks, a2_mks, pr_mks, t1_mks, t2_mks)
        totalmarks = (A1_mks / int(G.A1[0])) * 7.5 + (A2_mks / int(G.A2[0])) * 7.5 + (PR_mks / int(G.Project[0])) * 25 + (T1_mks / int(G.Test1[0])) * 30 + (T2_mks / int(G.Test2[0])) * 30
        grade = round(totalmarks, 2) 
            
        band = C.computeBand(grade, G, C, option) 
        # print(band)
            
        self.final_dict[id] = [id, lname, fname, a1_mks, a2_mks, pr_mks, t1_mks, t2_mks, grade, band]
        self.final_list.append({"id":id, "lname":lname, "fname":fname, "a1_mks": a1_mks, "a2_mks":a2_mks, "pr_mks":pr_mks, "t1_mks":t1_mks, "t2_mks":t2_mks, "grade":grade, "band":band})
        
    def get_name(self, id, G, C, mydict=[]):
        name = []
        for val in mydict.keys():
            if(val == id):
                value = mydict[id]
                (lastname, firstname) = value.split(",")
                name.append(lastname)
                name.append(firstname[1:])
                return name
    
    def getmarks(self, id, G, C, mydict={}):
        count = 0
        score = 0
        for val in mydict.keys():
            if(val == id):
                value = mydict[id]
                (lastname, firstname, mark) = value.split(",")
                count = 1
                score = mark
        if(count == 1):
            return score
        else:
            # return ' '
            return 'zero'
    
    def computeBand(self, grade, G, C, flag):
        band = 'F'
        # print(flag)
        
        passval = flag
        N_factor = round(((100 - passval) / 7), 2)
        # print(N_factor)
        
        C_band = passval + (N_factor * 1)
        Bminus = passval + (N_factor * 2)
        B_band = passval + (N_factor * 3)
        Bplus = passval + (N_factor * 4)
        Aminus = passval + (N_factor * 5)
        A_band = passval + (N_factor * 6)
        Aplus = passval + (N_factor * 7)
        
        if(grade < passval):
            band = 'F'
        elif(grade >= passval) and (grade < C_band):
            band = 'C'
        elif(grade >= C_band) and (grade < Bminus):
            band = 'B-'
        elif(grade >= Bminus) and (grade < B_band):
            band = 'B'
        elif(grade >= B_band) and (grade < Bplus):
            band = 'B+'
        elif(grade >= Bplus) and (grade < Aminus):
            band = 'A-'
        elif(grade >= Aminus) and (grade < A_band):
            band = 'A'
        else:
            band = 'A+'
        return band
        
    def Sort_alternate_column(self, G, C):
        order = int(input("Choose sort orders - 1 or 2 :- \n1.LT (last name)  \n2.GR (numeric grade)\n"))
        
        if(order == 1):
            print("Sorting By Last Name\n")
            print("Pass/ Fail point : 50")
            C.getSort(G, C, order)
        elif(order == 2):
            print("Sorting By Numeric Grade\n")
            print("Pass/ Fail point : 50")
            C.getSort(G, C, order)
        else:
            print("Enter correct option : 1.LT (last name) and 2.GR (numeric grade) : 1 or 2\n")
            C.Sort_alternate_column(G, C)
         
        self.final_list = []
        self.final_dict.clear
        # print(self.final_list)    
        # print(self.final_dict)
        
    def getSort(self, G, C, order):
        
        print("%-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s" % ("ID", "LN" , "FN", "A1", "A2", "PR", "T1", "T2", "GR", "FL"))
        self.final_list = []

        option = 50
        for id in G.dict_file.keys():
            C.getgrade(id, G, C, option)
            
        if(order == 1):
            sort = 'lname'
            for val in sorted(self.final_list, key=operator.itemgetter(sort)):
                dict = val
                C.publish(G, C, dict)
        else:
            sort = 'grade'
            for val in sorted(self.final_list, key=operator.itemgetter(sort), reverse=True):
                dict = val
                C.publish(G, C, dict)
        
    def publish(self, G, C, dict={}):
        id = dict['id']
        lname = dict['lname'] 
        fname = dict['fname'] 
        a1_mks = dict['a1_mks']  
        a2_mks = dict['a2_mks']
        pr_mks = dict['pr_mks']
        t1_mks = dict['t1_mks']
        t2_mks = dict['t2_mks']
        grade = dict['grade']
        band = dict['band']
        if(a1_mks == 'zero'): 
            a1_mks = ' '
        if(a2_mks == 'zero'): 
            a2_mks = ' '
        if(pr_mks == 'zero'): 
            pr_mks = ' '
        if(t1_mks == 'zero'): 
            t1_mks = ' '
        if(t2_mks == 'zero'): 
            t2_mks = ' '
        print("%-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s" % (id, lname, fname, a1_mks, a2_mks, pr_mks, t1_mks, t2_mks, grade, band))
             
    # task 5   
    def Change_point(self, G, C):
        
        option = int(input("Enter the new Pass/Fail point :"))
        
        print("Pass/ Fail point :", option)
        for id in G.dict_file.keys():
            C.getgrade(id, G, C, option)
            
        C.printGrade()    
        
    # Task 6
    def Exit(self):
        print("Good Bye")
        sys.exit()
        
