
class Bank(object):
	def __init__(self, balance = 0, customers = [], employees = []):
		self.customers = customers
		self.employees = employees
		self.balance = balance

	def add_customer(self, customer):
		if not customer in self.customers:
			self.customers.append(customer)
			self.balance += customer.balance

	def remove_customer(self, customer):
		if customer in self.customers:
			self.customers.remove(customer)
			self.balance -= customer.balance

	def check_balance(self):
		return self.balance

	def update_balance(self, balance):
		self.balance += balance


