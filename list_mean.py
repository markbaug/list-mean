def list_mean(inputlist):
	sum=0.0
	size=len(inputlist)
	index=0
	while index<=size-1:
		sum=sum+inputlist[index]
		index=index+1
	answer=sum/size
	return answer