# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 10:23:47 2025

@author: lab
"""
class Employee:
    empCount = 0
    def __int__(self,name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount +=1
    def displayCount(self):
        print("Total Employee %d", Employee.empCount)
        
    def displayEmployee(self):
        print("Name : ", self.name, ",Salary: ", self.salary)
        
empledo1 = Employee("Pedro", 800)
print("Total Employee %d" % Employee.empCount)