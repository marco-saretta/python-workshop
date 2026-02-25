import os
import sys
import json
import math

x=10
y =20
z= x+y

def Calculate_Sum(A,B,C):
    result=A+B+C
    return result

def fetchUserData(userId):
    userData = {}
    userData['id'] = userId
    userData['name'] = 'John'
    userData['age'] = 25  
    userData['score'] = 100
    return userData

class user_account:
    def __init__(self,username,Password,Email):
        self.username=username
        self.Password=Password
        self.Email=Email
        self.isActive=True
    
    def CheckPassword(self,inputPassword):
        if inputPassword==self.Password:
            return True
        else:
            return False
    
    def Deactivate(self):
        self.isActive=False
        print('Account deactivated')


def process_list(myList):
    output=[]
    for i in range(len(myList)):
        if myList[i]>0:
            output.append(myList[i]*2)
        else:
            output.append(0)
    return output


def load_config(filePath):
    f = open(filePath)
    data = json.load(f)
    f.close()
    return data


def divide(a,b):
    if b==0:
        print('Cannot divide by zero')
        return None
    return a/b


longString = 'This is a very long string that goes well beyond the recommended line length of 79 characters in PEP8 and should be wrapped'

scores = [95,82,67,40,55,78,91]
passing=[]
failing=[]
for s in scores:
    if s>=60:
        passing.append(s)
    else:
        failing.append( s )

print( 'Passing:', passing )
print('Failing:',failing)