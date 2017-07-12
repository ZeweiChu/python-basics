class Customer(object):
	def __init__(self, ID, name, bank, balanace=0):
		self.ID = ID
		self.name = name
		self.balanace = balanace
		self.bank = bank

	def update_balance(self, balanace):
		self.balanace += balanace
		self.bank.update_balance(balanace)

	def get_info(self):
		return "customer name: {}, bank name: {}"