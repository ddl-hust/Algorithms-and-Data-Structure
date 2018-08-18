def quickSort(alist):
	#函数递归调用helper
	quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
	#类似merge sort
	if first <last:
		splitpoint=partition(alist,first,last)
		quickSortHelper(alist,first,splitpoint-1) #左半边调用
		quickSortHelper(alist,splitpoint+1,last)
def partition(alist,first,last):
	pivotvalue=alist[first]
	
	leftmark=first+1
	rightmark=last

	done=False
	while not done:
		while leftmark<=rightmark and alist[leftmark]<=pivotvalue:
			leftmark+=1
		while leftmark<=rightmark and alist[rightmark]>=pivotvalue:
			rightmark-=1
		if rightmark<leftmark:
			done =True
		else:
			#交换左右半区 
			alist[leftmark],alist[rightmark]=alist[rightmark],alist[leftmark]
	alist[first],alist[rightmark]=alist[rightmark],alist[first]
	return rightmark
alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)