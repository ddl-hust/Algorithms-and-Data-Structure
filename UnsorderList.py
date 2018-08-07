from Node import *
class UnsortedList:
	def __init__(self):
		self.head=None
	#检测链表是否为空
	def isEmpty(self):
		return self.head==None
	#理解
	def add(self,item):
		temp=Node(item)
		temp.setNext(self.head)
		self.head=temp
	#遍历返回节点个数
	def size(self):
		current=self.head
		count=0
		while current!=None:
			count+=1
			current=current.getNext()
		return count
	#寻找特定元素
	def search(self,item):
		current=self.head
		found=False
		while current !=None and not found:
			if current.getData()==item:
				found=True
			else:
				current=current.getNext()
		return found
mylist=UnsortedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
print( mylist.search(26))