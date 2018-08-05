from Stack import *
def divideBy2(decnumber):
	remstack=Stack()
	while decnumber>0:
		rem =decnumber%2
		remstack.push(rem)
		decnumber=decnumber//2
	binstring=""
	while not remstack.isEmpty():
		binstring=binstring+str(remstack.pop())
	return binstring
print(divideBy2(6))