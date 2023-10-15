def insert(nums:list)->list:
	size=len(nums)
	for i in range(1,size):
		current=nums[i]
		j=i-1
		while j>=0 and nums[j]>current:
			nums[j+1]=nums[j]
			j-=1
		nums[j+1]=current
	return nums


