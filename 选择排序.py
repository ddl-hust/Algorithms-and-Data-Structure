#注意与冒泡排序的区别 每次遍历只进行一次交换
def selctionSort(alist):
	for fileslot in range(len(alist)-1,0,-1):
		positionMax=0
		#找到位置最大的item
		for location in range(1,fileslot+1):
			if alist[location]>alist[positionMax]:
				positionMax=location
		alist[fileslot],alist[positionMax]=alist[positionMax],alist[fileslot]
alist=[54,26,93,17,77,31,44,55,20]
selctionSort(alist)
print(alist)