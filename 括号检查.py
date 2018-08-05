from Stack import *
def parChecker(string):
	"""using stack to implent check
	"""
	s=Stack()
	balanced= True
	index=0
	while index<len(string) and balanced:
		symbol=string[index]
		if symbol in "([{":
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced=False
			else:
				top=s.pop()
				if not matches(top,symbol):
					balanced=False
		index+=1
	if balanced and s.isEmpty():
		return True
	else:
		return False
def matches(open,close):
	opens="[{("
	closes="]})"
	return opens.index(open)==closes.index(close)
print(parChecker('[{()}]'))
