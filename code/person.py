from abc import ABC, abstractmethod

class Person(ABC):
	@abstractmethod
	def __init__(self, name, ID):
		self.name = name
		self.ID = ID

	@abstractmethod
	def get_info(self):
		return "name: {}".format(self.name)

	def __eq__(self, other):
		return self.ID == other.ID

# tongjun = Person("Tongjun", "11")
# print(tongjun.get_info())

class Student(Person):
	def __init__(self, name, ID, level=0):
		super().__init__(name, ID)
		self.level = level

	def get_info(self):
		return "{}, level: {}".format(super().get_info(), self.level)

	def take_exam(self, grade):
		if grade.upper() in ["A", "B", "C"]:
			self.level += 1
		return self.level

	def graduate(self):
		print(self.get_info())
		if self.level >= 12:
			print("Congratulations! You've graduated from Julyedu.")
			return True
		else:
			print("Sorry, you need to pass {} extra exams!".format(12 - self.level))
			return False

hongyu = Student("Hongyu", 10, 3)
print(hongyu.get_info())
hongyu.take_exam("A")

print(hongyu.get_info())
hongyu.graduate()
hongyu.take_exam("B")
hongyu.take_exam("B")
hongyu.take_exam("B")
hongyu.take_exam("B")
hongyu.take_exam("B")
hongyu.take_exam("B")
hongyu.take_exam("B")
hongyu.take_exam("B")
hongyu.take_exam("B")
hongyu.take_exam("B")
hongyu.take_exam("B")
hongyu.take_exam("B")
hongyu.take_exam("B")
hongyu.take_exam("B")
print(hongyu.get_info())
hongyu.graduate()




