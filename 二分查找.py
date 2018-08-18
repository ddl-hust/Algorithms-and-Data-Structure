def binarySearch(alist,item):
	first=0
	last=len(alist)-1
	found=False
	while first<=last and not found:
		midpoint=(first+last)//2
		if alist[midpoint]==item:
			found=True
		else:
			if alist[midpoint]>item:
				last=midpoint-1
			else:
				first=midpoint+1

	return found
	#时间复杂度 O(logn)
def recurion_BinarySearch(alist,item):
	if len(alist)==0:
		return False
	else:
		midpoint=len(alist)//2
		if alist[midpoint]==item:
			return True
		else:
			if alist[midpoint]>item:
				return recurion_BinarySearch(alist[:midpoint],item) #slice 的时间复杂度 能通过index 进一步改进
			else:
				return recurion_BinarySearch(alist[midpoint+1:],item)
	return 
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(recurion_BinarySearch(testlist,12))