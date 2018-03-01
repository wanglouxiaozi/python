#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

class Employee:
	'所有员工的基类'
	empCount = 0
	
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1

	def displayCount(self):
		print "Total Employee %d" % Employee.empCount

	def displayEmployee(self):
		print "Name : ", self.name, ", Salary: ", self.salary

def test1(emp2):
	print "="*100
	print hasattr(emp2, 'age') #如果存在'age'属性返回True
	setattr(emp2, 'age', 8) #添加属性'age'值为8
	print hasattr(emp2, 'age') #如果存在'age'属性返回True
	print getattr(emp2, 'age') #返回'age'属性的值
#	delattr(emp2, 'age') #删除属性'age'
#	print hasattr(emp2, 'age') #如果存在'age'属性返回True
	print "="*100

def __main():

	"创建 Employee 类的第一个对象"
	emp1 = Employee("Zara", 2000)
	"创建 Employee 类的第二个对象"
	emp2 = Employee("Manni", 5000)
	emp1.displayEmployee()
	emp2.displayEmployee()
	print "Total Employee %d" % Employee.empCount
	print emp1.salary
 	emp1.salary = 1000
	print emp1.salary
	emp1.displayEmployee()
	emp1.age = 7 #添加一个 'age' 属性
	emp1.age = 8 #修改 'age' 属性
	#del emp1.age '''删除age 属性 '''
	print emp1.age
	test1(emp2)
	print hasattr(emp2, 'age')
if __name__ == "__main__":
	__main()
