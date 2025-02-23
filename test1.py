#import important library
from tabulate import tabulate

#welcome the user in software
print(" ")
print("Welcome to SmartSched!!!")

#give the instruction to the user
print(" ")
print("You can schedule a maximum of 8 subjects at a time")
print("The minimum number of subjects is 4")
print("Only 1 or 2 days off are allowed")
print("A minimum of 4 lectures is allowed, and a maximum of 8 lectures")

#take user inputs like:
#number of subjects, study days in a week, lectures in a day
subjectnum = int(input("1. Enter the number of subjects you want to schedule: "))
studyday = int(input("2. Enter the study days in a week (5/6): "))
lectureinday = int(input("3. Enter the number of lectures in a week: "))

#collect the names of subjects based on the number of subjects
if subjectnum == 4:
    s1 = input("Enter the 1st subject name: ")
    s2 = input("Enter the 2nd subject name: ")
    s3 = input("Enter the 3rd subject name: ")
    s4 = input("Enter the 4th subject name: ") 

    if studyday == 5:
        print("You have 2 days off in your schedule.")

        if lectureinday == 4:
            tt = [
                ["Lectures", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                ["lec-1", s1, s2, s3, s4, s1, "off", "off"],
                ["lec-2", s2, s3, s4, s1, s2, "off", "off"],
                ["Break", "Break", "Break", "Break", "Break", "off", "off"],
                ["lec-3", s3, s4, s1, s2, s3, "off", "off"],
                ["lec-4", s4, s1, s2, s3, s4, "off", "off"]
            ]
            print(tabulate(tt, headers="firstrow", tablefmt="grid"))

        elif lectureinday == 5:
            tt = [
                ["Lectures", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                ["lec-1", s1, s2, s3, s4, s1, "off", "off"],
                ["lec-2", s2, s3, s4, s1, s2, "off", "off"],
                ["lec-3", s3, s4, s1, s2, s3, "off", "off"],
                ["Break", "Break", "Break", "Break", "Break", "off", "off"],
                ["lec-4", s4, s1, s2, s3, s4, "off", "off"],
                ["lec-5", s1, s2, s3, s4, s1, "off", "off"]
            ]
            print(tabulate(tt, headers="firstrow", tablefmt="grid"))

    elif studyday == 6:
        print("You have 1 day off in your schedule.")

    else:
        print("!!!Please enter a valid input!!!")

elif subjectnum == 5:
    s1 = input("Enter the 1st subject name: ")
    s2 = input("Enter the 2nd subject name: ")
    s3 = input("Enter the 3rd subject name: ")
    s4 = input("Enter the 4th subject name: ")
    s5 = input("Enter the 5th subject name: ")

    # Logic to handle subject scheduling for 5 subjects (similar to the above)

elif subjectnum == 6:
    s1 = input("Enter the 1st subject name: ")
    s2 = input("Enter the 2nd subject name: ")
    s3 = input("Enter the 3rd subject name: ")
    s4 = input("Enter the 4th subject name: ")
    s5 = input("Enter the 5th subject name: ")
    s6 = input("Enter the 6th subject name: ")

    # Logic to handle subject scheduling for 6 subjects (similar to the above)

elif subjectnum == 7:
    s1 = input("Enter the 1st subject name: ")
    s2 = input("Enter the 2nd subject name: ")
    s3 = input("Enter the 3rd subject name: ")
    s4 = input("Enter the 4th subject name: ")
    s5 = input("Enter the 5th subject name: ")
    s6 = input("Enter the 6th subject name: ")
    s7 = input("Enter the 7th subject name: ")

    # Logic to handle subject scheduling for 7 subjects (similar to the above)

elif subjectnum == 8:
    s1 = input("Enter the 1st subject name: ")
    s2 = input("Enter the 2nd subject name: ")
    s3 = input("Enter the 3rd subject name: ")
    s4 = input("Enter the 4th subject name: ")
    s5 = input("Enter the 5th subject name: ")
    s6 = input("Enter the 6th subject name: ")
    s7 = input("Enter the 7th subject name: ")
    s8 = input("Enter the 8th subject name: ")

    # Logic to handle subject scheduling for 8 subjects (similar to the above)

else:
    print("!!!Please enter a valid input!!!")
