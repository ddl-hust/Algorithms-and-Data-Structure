#不能用递归解决第三种情况，即最大子序列穿过左右子序列
def FindMaxCrossSubarray(alist,low,mid,high):
	left_sum=-float("inf")
	total_sum=0
	max_left=mid
	i=mid
	for i in range(mid,low-1,-1):
		total_sum+=alist[i]
		if total_sum>left_sum:
			left_sum=total_sum
			max_left=i
	# while low<=i:
	# 	total_sum+=alist[i]
	# 	if total_sum>max_left:
	# 		left_sum=total_sum
	# 		max_left=i
	# 	i-=1
	 
	right_sum=-float("inf")
	total_sum=0
	for i in range(mid+1,high+1):
		total_sum+=alist[i]
		if total_sum>right_sum:
			right_sum=total_sum
			max_right=i
	# while high>=i:
	# 	total_sum+=alist[i]
	# 	if total_sum>right_sum:
	# 		right_sum=total_sum
	# 		max_right=i
	# 	i+=1
	return (max_left,max_right,left_sum+right_sum)

def FindMaxSubarray(alist,low,high):
	#递归基本条件
	if low==high:
		return(low,high,alist[low])
	mid=int((low+high)/2)
	left_low,left_high,left_sum=FindMaxSubarray(alist,low,mid)
	right_low,right_high,right_sum=FindMaxSubarray(alist,mid+1,high)
	cross_low,cross_high,cross_sum=FindMaxCrossSubarray(alist,low,mid,high)
	if left_sum>=right_sum and left_sum>=cross_sum:
		return (left_low,left_high,left_sum)
	elif right_sum>=left_sum and right_sum>=cross_sum:
		return (right_low,right_high,right_sum)
	else:
		return (cross_low,cross_high,cross_sum)
test_list=[13,-3,-25,20,-3,16,-23,18,20,-7,12,-5,-22,15,-4,7]
print (FindMaxSubarray(test_list,0,len(test_list)-1))