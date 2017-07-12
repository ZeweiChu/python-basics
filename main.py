from code.employee import Employee
from code.company import *

if __name__ == "__main__":
	july = Employee("July", 1, "CEO", 99999999)
	# print(july.get_info())
	zewei = Employee("Zewei", 2, "Lecturer", 1, july)
	# print(zewei.get_info())

	c = Company("Julyedu")
	c.hire(july)
	c.hire(zewei)

	han = Employee("Han Xiaoyang", 3, "Lecturer", 1000000, july)
	c.hire(han)

	print(c.get_info())

	print("Firing Zewei!!!")
	c.fire(zewei)
	print(c.get_info())

	print("Firing Zewei!!!")
	c.fire(zewei)
	print(c.get_info())

	c.hire(zewei)
	print(c.get_info())	

	# sublime
	# namespace


