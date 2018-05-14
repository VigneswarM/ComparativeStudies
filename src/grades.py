import sys
import os
import compute as C

#print(sys.path)


#fp = open('D://Workspace//python//Assignment1//data//a1.txt', 'r') 


def welcome_main():
    print("welcome \n")
    print("1> Display individual component")
    print("2> Display component average")
    print("3> Display Standard Report")
    print("4> Sort by alternate column")
    print("5> Change Pass/Fail point")
    print("6> Exit")
    user_input = int(input("\nselect your option (1-6) :"))
    
    if (user_input <=0) or (user_input >6)  :
        user_input = int(input("Wrong option - select option between (1-6) :"))
    else:    
        C.task(user_input)
    print("***end of task ***")
    check = int(input("Do You Wish to Continue 1-Yes  2-No, Enter 1 or 2:" ))
    if(check ==1):
        welcome_main()
    else :
        C.task(6)
    
    
print(os.getcwd())
welcome_main()


    