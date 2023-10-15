def pick_repeat(nums:list[int]):
	for i in range(len(nums)):
		while i!=nums[i]:
			# print(nums[i])
			if nums[i]==nums[nums[i]]:
				return nums[i]
			else:
				tmp=nums[i]
				nums[i],nums[tmp]=nums[tmp],nums[i]
				# tmp=nums[i]
				# nums[i]=nums[tmp]
				# nums[tmp]=tmp

	return None
nums=[2, 3, 1, 0, 2, 5]
print("start")
print(pick_repeat(nums))