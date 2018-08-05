from Stack import *
def parChecker(string):
	"""使用堆栈实现括号完整检查
	"""
	s=Stack()
	balanced= True
	index=0
	while index<len(string) and balanced:
		symbol=string[index]
		if symbol=="(":
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced=False
			else:
				s.pop()
		index+=1
	if balanced and s.isEmpty():
		return True
	else:
		return False
print(parChecker('((()))'))
