def myapplication():
    print("enter the following info below")
    stdname = input("student name is: ")
    stdage = input("student age is: ")
    gender = input("Gender: ")
    dob = input("date of birth: ")
    address = input( "Address:")
    fathername = input("Father's Name: ")
    mothername = input("Mother's Name: ")
    fatheroccu = input("Father's occupation is: ")
    citizen = input("spanish citizen:")
    if citizen == "yes":

        print("spanish")
    else:
        print("not citizen")
    studentgrade = input("student grade is: ")
    division = input("what division are you on fifa: ")
    majorproject = input("major project: ")
    print("student name is: ",stdname)
    print("student age is: ",stdage)
    print("Gender: ",gender)
    print("date of birth: ",dob)
    print("Address:",address)
    print("Father's Name: ",fathername)
    print("Mother's Name: ",mothername)
    print("Father's occupation is: ",fatheroccu)
    print("spanish citizen:",citizen)
    print("student grade is: ",studentgrade )
    print("what division are you on fifa: ",division)
    print("major project: ", majorproject)

myapplication()


"""
from math import *
x = input("enter your name: ")
print("hi  " + x + "!")