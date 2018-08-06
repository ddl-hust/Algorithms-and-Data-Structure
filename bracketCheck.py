#调用栈抽象类
from Stack import *
def Checker(string):
	s=Stack()
	flag=True #括号平衡标志位
	index=0
	while index<len(string) and flag:
		symbol =string[index]
		if symbol in "({[":
			s.push(symbol)
		else:
			if s.isEmpty():
				flag=False
			#当为右括号的时候 配对
			else:
				top =s.pop()
				if not matches(top,symbol):
					flag=False
		index+=1
	if flag and s.isEmpty():
		return True
	else:
		return False


def matches(open,close):
	opens="[{("
	closes="]})"
	return opens.index(open)==closes.index(close)

print (Checker('(()'))	