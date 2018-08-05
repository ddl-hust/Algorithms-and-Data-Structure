from Stack import *
def convert(infixexpre):
	#用一个词典储存不同运算符的优先级，建立表达式到数字的映射
	prec={}
	prec["*"]=3
	prec["/"]=3
	prec["-"]=2
	prec["+"]=2
	prec["("]=1 #左括号的优先级最低
	#将运算符储存在栈里面
	opstack=Stack()
	#输出后缀表达式存在列表
	postfixList=[]
	#将输入的string 转化为list
	tokenlist=infixexpre.split()
	for token in tokenlist:
		#如果标记是操作数，将其附加到输出列表的末尾
		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789": #有简便的表达式嘛？
			postfixList.append(token)
		#如果标记是左括号，将其压到 opstack
		elif token=="(":
			opstack.push(token)
		#如果标记是右括号，则弹出 opstack，直到删除相应的左括号。将每个运算符附加到输出列表的末尾。
		elif token==")":
			top=opstack.pop()
			while top!='(':
				postfixList.append(top)
				top=opstack.pop()
		else:
			#如果标记是运算符，*，/，+或 - ，将其压入 opstack
			#但是，首先删除已经在 opstack 中具有更高或相等优先级的任何运算符，并将它们加到输出列表中
			while (not opstack.isEmpty()) and (prec[opstack.peek()>=prec[token]]):
				postfixList.append(opstack.pop())
				opstack.push(token)
	while not opstack.isEmpty():
		postfixList.append(opstack.pop())
	return " ".join(postfixList)
print (convert("A*B+C*D"))
