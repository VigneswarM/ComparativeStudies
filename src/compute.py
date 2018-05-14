import sysconfig
import os
import sys
#import grades as G


a1 = open('a1.txt').read().split("\n")
a2 = open('a2.txt').read().split("\n")
pr = open('project.txt').read().split("\n")
t1 = open('test1.txt').read().split("\n")
t2 = open('test2.txt').read().split("\n")

dict_file = {}
with open("class.txt") as f:
    for line in f:
       (key, val1,val2) = line.split("|")
       dict_file[int(key)] = val2[:-1] +","+val1

print(dict_file)

dict_file_a1 ={}

for id in dict_file.keys():
        for x in a1[1:]:
            temp=x.split("|")
            if(int(temp[0])==id):
                sid =id
                name=dict_file[id]
                mark = temp[1]
                dict_file_a1[int(sid)]= name+","+mark
                

print(dict_file_a1)
    
     

def task(taskId):
    print("inside task")
    task = taskId
    if(task == 1):
        Display_individual_component()
    elif(task == 2):
        Display_component_average()
    elif(task == 3):
        Display_Standard_Report()
    elif(task == 4):
        Sort_alternate_column()
    elif(task == 5):
        Change_point()
    else :
        Exit()
    
    
        
def get_input():
    user_input = input("Choose the component name (A1, A2, PR, T1, or T2) :")
    if(user_input == "A1") or (user_input == "a1"):
        print("A1" + " grades "+a1[0])
        return "a1"
    elif(user_input == "A2") or (user_input == "a2"):
        print("A2" + " grades "+a2[0])
        return "a2"
    elif(user_input == "PR") or (user_input == "pr"):
        print("Project" + " grades "+pr[0])
        return "pr"
    elif(user_input == "T1") or (user_input == "t1"):
        print("Test1" + " grades "+t1[0])
        return "t1"
    elif(user_input == "T2") or (user_input == "t2"):
        print("Test2" + " grades "+t2[0])
        return "t2"
    else:
        print("Invalid input enter from choice (A1, A2, PR, T1, or T2) :")
        get_input()
    
 
 
def getavg(component):
    sum = 0
    count =0
    for x in component[:]:
        if(count==0):
            count = count +1
            number = x.split("|")
            print(number)
            #sum = number[1] + sum
            print(sum)
             
    return 0
    
     
 
def Display_individual_component():
    print("inside option 1")
    val =get_input()
        
   
     
 
def Display_component_average():
    print("inside option 2")
    val =get_input()
    average = getavg(val)
    print(average)
    
    
    
    print("********************")
    #G.welcome_main()
    
def Display_Standard_Report():
    print("inside option 3")
    print("********************")
    #G.welcome_main()
    
def Sort_alternate_column():
    print("inside option 4")
    print("********************")
    #G.welcome_main()
    
    
def Change_point():
    print("inside option 5")
    print("********************")
    #G.welcome_main()
    

def Exit():
    print("Good Bye")    
    sys.exit()
    

        