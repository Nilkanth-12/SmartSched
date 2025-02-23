#import important library
from tabulate import tabulate

#welcome a user in software

print(" ")
print("Welcome to print SmartSched!!!")

#give the instruction to user

print(" ")
print("You can schedule maximum 8 subject at a time")
print("Number of subject is minimum 4 ")
print("only 1 or 2 days off can allowed ")
print("minimum 4 lecture allowed and maximum 8 lecture")

#take use full inputs from user like:-
#number of subject
#study day in a week
#lectures in a day

subjectnum = int(input("1.Enter the number of subject you want to schedule:- "))
studyday = int(input("2.Enter the study day in a week(5/6):- "))
lectureinday = int(input("3.Enter the number of lecture in a week:- "))

#collect name of subjects from user with us of if else 

if subjectnum == 4:
    s1 = input("Enter 1st the subject name:- ")
    s2 = input("Enter 2nd the subject name:- ")
    s3 = input("Enter 3rd the subject name:- ")
    s4 = input("Enter 4th the subject name:- ") 

    if studyday == 5:
        print("you have 2 week off in your Schedule or Timetable")

        if lectureinday == 4:
            tt = [
                ["lectures","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","sunday"],
                ["lec-1",s1,s2,s3,s4,s1,"off","off"],
                ["lec-2",s2,s3,s4,s1,s2,"off","off"],
                ["Break","Break","Break","Break","Break","off","off"],
                ["lec-3",s3,s4,s1,s2,s3,"off","off"],
                ["lec-4",s4,s1,s2,s3,s4,"off","off"]
            ]
            print(tabulate(tt, headers="firstrow", tablefmt="grid"))


        elif lectureinday == 5:  
               tt = [
                ["lectures","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","sunday"],
                ["lec-1",s1,s2,s3,s4,s1,"off","off"],
                ["lec-2",s2,s3,s4,s1,s2,"off","off"],
                ["lec-3",s3,s4,s1,s2,s3,"off","off"],
                ["Break","Break","Break","Break","Break","off","off"],
                ["lec-4",s4,s1,s2,s3,s4,"off","off"],
                ["lec-5",s1,s2,s3,s4,s1,"off","off"]
            ]
            print(tabulate(tt, headers="firstrow", tablefmt="grid"))
        
        elif lectureinday == 6:  
             tt = [
                ["lectures","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","sunday"],
                ["lec-1",s1,s2,s3,s4,s1,"off","off"],
                ["lec-2",s2,s3,s4,s1,s2,"off","off"],
                ["lec-3",s3,s4,s1,s2,s3,"off","off"],
                ["Break","Break","Break","Break","Break","off","off"],
                ["lec-4",s4,s1,s2,s3,s4,"off","off"],
                ["lec-5",s1,s2,s3,s4,s1,"off","off"]
            ]
            print(tabulate(tt, headers="firstrow", tablefmt="grid"))

        elif lectureinday == 7:  
            print("rg")  

        elif lectureinday == 8:  
            print("rt")   

        else:
            print("error")    

    elif studyday == 6:
        print("you have 1 week off in your schedule ot Timetable")   

    else :
        print("!!!Please enter the valid input!!!")    




elif subjectnum == 5:
    s1 = input("Enter 1st the subject name:- ")
    s2 = input("Enter 2nd the subject name:- ")
    s3 = input("Enter 3rd the subject name:- ")
    s4 = input("Enter 4th the subject name:- ")
    s5 = input("Enter 5th the subject name:- ")

elif subjectnum == 6:
    s1 = input("Enter 1st the subject name:- ")
    s2 = input("Enter 2nd the subject name:- ")
    s3 = input("Enter 3rd the subject name:- ")
    s4 = input("Enter 4th the subject name:- ")
    s5 = input("Enter 5th the subject name:- ")    
    s6 = input("Enter 6th the subject name:- ")    

elif subjectnum == 7:
    s1 = input("Enter 1st the subject name:- ")
    s2 = input("Enter 2nd the subject name:- ")
    s3 = input("Enter 3rd the subject name:- ")
    s4 = input("Enter 4th the subject name:- ")
    s5 = input("Enter 5th the subject name:- ")    
    s6 = input("Enter 6th the subject name:- ")       
    s7 = input("Enter 7th the subject name:- ")       
    
elif subjectnum == 8:
    s1 = input("Enter 1st the subject name:- ")
    s2 = input("Enter 2nd the subject name:- ")
    s3 = input("Enter 3rd the subject name:- ")
    s4 = input("Enter 4th the subject name:- ")
    s5 = input("Enter 5th the subject name:- ")    
    s6 = input("Enter 6th the subject name:- ")       
    s7 = input("Enter 7th the subject name:- ")
    s8 = input("Enter 8th the subject name:- ")

else:
    print("!!!Please enter valid input!!!")    