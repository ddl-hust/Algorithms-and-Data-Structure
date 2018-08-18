def shellsort(alist):
	sublistcount=len(alist)//2
	while sublistcount>0:
		for start_position in range(sublistcount):
			gapIndertSort(alist,start_position,sublistcount)
		print ("after incremnet of size",sublistcount,"the list is ",alist)
		sublistcount=sublistcount//2
#插入排序的泛化版 当gap==1时 为标准插入排序
def gapIndertSort(alist,start_position,gap):
	for i in range(start_position+gap,len(alist),gap):
		currentvalue=alist[i]
		position=i
		while position>=gap and alist[position-gap]>currentvalue:
			alist[position]=alist[position-gap]
			position=position-gap
		alist[position]=currentvalue
alist = [54,26,93,17,77,31,44,55,20]
shellsort(alist)
print(alist)