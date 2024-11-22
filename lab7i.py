#!/usr/bin/env python3
# Student ID: ivassiljenko
def function1():
    global schoolName
    schoolName = 'SICT'
    print('print() in function1 on schoolName:', schoolName)

def function2():
    global schoolName
    schoolName = 'SSDO'
    print('print() in function2 on schoolName:', schoolName)

schoolName = 'Seneca'
print('print() in main on schoolName:', schoolName)  # Main scope print
function1()  # Call function1, should change global schoolName to 'SICT'
print('print() in main on schoolName:', schoolName)  # Main scope print after function1
function2()  # Call function2, should change global schoolName to 'SSDO'
print('print() in main on schoolName:', schoolName)  # Main scope print after function2
