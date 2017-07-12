class Company(object):
	def __init__(self, name, employees=[]):
		self.name = name
		self.employees = employees

	def hire(self, employee):
		if not employee in self.employees:
			self.employees.append(employee)

	def fire(self, employee):
		if employee in self.employees:
			self.employees.remove(employee)

	def get_info(self):
		res = "Company: {}, employees: ".format(self.name)
		for employee in self.employees:
			res += ", {}".format(employee.get_info())
		return res






