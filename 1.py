class NegativeTotalError(Exception):
	def __init__(self):
		pass

class Charge:
	def __init__(self,value = 0.0):
		self._value = value

	@property
	def value(self):
		return round(self._value,2)

class Account:
	def __init__(self,total = 0.0, charges = []):
		self._charges = charges
		self._total = total

	def __iter__(self):
		return iter(self._charges)
		
	def add_charge(self,new_charge):
		try:
			if (self._total + new_charge.value < 0):
				raise NegativeTotalError
		except NegativeTotalError:
			print("Negative total, try another charge")
		else:
			self._total += new_charge.value
			self._charges.append(new_charge)
			print("Added _charge is :"+str(new_charge.value))
			print("Total is: "+str(self._total))

def main():
	b = Account()
	b.add_charge(Charge(5))
	b.add_charge(Charge(10.2))
	b.add_charge(Charge(-25.6))
	b.add_charge(Charge(10.2))

if __name__ == '__main__':
    main()