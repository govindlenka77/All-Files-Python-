def countSubarrays(nums, k):
    left = 0
    total = 0
    curr_sum = 0
    ans = 0

    for right in range(len(nums)):
        curr_sum += nums[right]
        while left <= right and  curr_sum * (right - left + 1)>= k:
            curr_sum -= nums[left]
            left += 1
        ans += (right - left + 1)
        print(ans,"--")
    
    return ans


print(countSubarrays([20,1,4,3,5],10))
