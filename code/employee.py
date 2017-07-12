from code.person import Person

class Employee(Person):
	def __init__(self, name, ID, title, salary, manager=None):
		super().__init__(name, ID)
		self.title = title
		self.salary = salary
		self.manager = manager

	def get_info(self):
		return "({}, title: {}, salary: {}, manager: {})".format(super().get_info(), self.title, self.salary, self.manager.get_info() if self.manager is not None else "")

