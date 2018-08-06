from Queue import *

def HotPotato(namelist,num):
	simqueue=Queue()
	#将元素入队
	for name in namelist:
		simqueue.enqueue(name)
	while simqueue.size()>1:
		#循环入队出对num次 把需要pop的元素推到front
		for i in range(num):
			simqueue.enqueue(simqueue.dequeue())
		simqueue.dequeue()
	return simqueue.dequeue()
print(HotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))