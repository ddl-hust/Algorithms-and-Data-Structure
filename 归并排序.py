#用递归方法 分而治之的方法进行排序
def mergesort(alist):
	#打印当前需要风分割list 
	print("splitting list",alist)
	if len(alist)>1:
		mid=len(alist)//2
		lefthalf=alist[:mid]
		righthalf=alist[mid:]
		mergesort(lefthalf)
		mergesort(righthalf)

		i=0
		j=0
		k=0
		while i<len(lefthalf) and j<len(righthalf):
			if lefthalf[i]<righthalf[j]:
				alist[k]=lefthalf[i]
				i+=1
			else:
				alist[k]=righthalf[j]
				j+=1
			k+=1
		while i<len(lefthalf):
			alist[k]=lefthalf[i]
			i+=1
			k+=1

		while j<len(righthalf):
			alist[k]=alist[j]
			j+=1
			k+=1

	print ("merging ", alist)
alist = [54,26,93,17,77,31,44,55,20]
mergesort(alist)
print(alist)
