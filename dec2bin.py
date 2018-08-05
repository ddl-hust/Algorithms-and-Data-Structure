from Stack import *
def divideBybase(decnumber,base):
	digits="0123456789ABCDEF"
	remstack=Stack()
	while decnumber>0:
		rem =decnumber%base
		remstack.push(rem)
		decnumber=decnumber//base
	binstring=""
	while not remstack.isEmpty():
		binstring=binstring+digits[remstack.pop()]
	return binstring
print(divideBybase(13,16))