def bubblesort(alist):
	for passnum in range(len(alist)-1,0,-1):
		for i in range(passnum):
			if alist[i]>alist[i+1]:
				#python 同时赋值
				alist[i],alist[i+1]=alist[i+1],alist[i]

"""
传统冒泡排序在最终位置知道前，每两项都需要比较 效率非常低下
通过z设置一个flag exchange 判定元素之间是否对比
"""
def improved_bubblesort(alist):
	exchange=True
	passnum=len(alist)-1
	while passnum>0 and exchange:
		exchange=False
		for i in range(passnum):
			if alist[i]>alist[i+1]: #在一次pass中比较了一次 exchange 置为true
				exchange=True
				alist[i],alist[i+1]=alist[i+1],alist[i]
		passnum-=1
alist = [54,26,93,17,77,31,44,55,20]
improved_bubblesort(alist)
print(alist)