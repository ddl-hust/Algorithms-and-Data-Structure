from Node import *
class UnsortedList:
	def __init__(self):
		self.head=None
	#检测链表是否为空
	def isEmpty(self):
		return self.head==None
	#理解 adds a new item to the list. It needs the item and returns nothing. Assume the
	#item is not already in the list
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
		current=self.head  ###为什么current 就是一个节点了
		found=False
		while current !=None and not found:
			if current.getData()==item:
				found=True
			else:
				current=current.getNext()
		return found
	#假定待删除元素存在
	def remove(self,item):
		current=self.head
		previous=None #The 指向当前节点的前一个节点,因为head前面没有节点，所以将previous设置为none
		found=False
		while not found:
			if current.getData()==item:
				found=True
			else:
				previous=current #这两句顺序很重要
				current=current.getNext()
		#特殊情况，当删除的元素为链表的第一个元素时，previous 此时为none
		#当需要删除的是链表的最后一个元素呢？
		if previous==None:
			self.head=current.getNext()
		else:
			previous.setNext(current.getNext())
	#adds a new item to the end of the list making it the last item in the collection. 
	#It needs the item and returns nothing. Assume the item is not already in the list.
	def append(self,item):
		current=self.head  #遍历直到最后一个元素
		while current.next!=None:
			current=current.getNext()
		temp=Node(item)
		current.setNext(temp)
	#有点问题
	def insert(self,item,position):
		count=0
		current=self.head
		previous=None
		while current!=None and not(count ==position):
			count+=1
			previous=current
			current=current.getNext()
		temp=Node(item)
		if previous==None:
			temp.setNext(self.head)
			self.head=temp
		else:
			temp.setNext(current)
			previous.setNext(temp)
	#returns the position of item in the list. It needs the item and returns the index.Assume the item is in the list.
	def index(self,item):
		count=0
		found =False
		current=self.head #引用别名
		while current!=None and not found:
			if current.getData()==item:
				found =True
			else:
				count+=1
				current=current.getNext()
		return count
	def pop(self,item,position):
		pass

mylist=UnsortedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.insert(26,0)
print( mylist.index(26))