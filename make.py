class CreditCard:
    def make payment(self, amount):
    class PredatoryCreditCard(CreditCard):
	OVERLIMIT_FEE = 5 # this is a class-level member
    def charge(self, price):
		success = super( ).charge(price)
    if not success:
		self. balance += PredatoryCreditCard.OVERLIMIT_FEE
	print(success);