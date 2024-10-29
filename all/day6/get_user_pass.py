#!/usr/bin/python3

def get_user_pass(admin):
    admin="secret"
    return admin

user_pass= get_user_pass("admin")
if user_pass==raw_input("please enter your password:"):   #user_pass will work in python3 it will directly assigns value secret   
    print("login successful")
else:
    print("password is incorrect")


#In python2 input()commnad gives the login successful if the user_pass is passed as input
#raw_input works correctly Gives error when user_pass given as input 







