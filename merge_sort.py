

def merge(low_nums: list, high_nums: list, len_low: int, len_high: int) -> list:
    
    res = []
    idx_low = 0
    idx_high = 0
    
    while(idx_low < len_low and idx_high < len_high):
        if low_nums[idx_low] > high_nums[idx_high]:
            res.append(high_nums[idx_high])
            idx_high = idx_high + 1
        else:
            res.append(low_nums[idx_low])
            idx_low = idx_low + 1

    while (idx_low < len_low):
        res.append(low_nums[idx_low])
        idx_low = idx_low + 1

    while(idx_high < len_high):
            res.append(high_nums[idx_high])
            idx_high = idx_high + 1           

    return res


def mergesort(nums: list, low: int, high: int) -> list:

   
    if high == 0:
        return nums
    
    mid = int(high /2)
    low_len = mid + 1
    low_nums = nums[:low_len]
    high_nums = [nums[high]] if high - mid - 1 == 0 else  nums[low_len : high + 1]

    print(f"{low_nums}, {high_nums}")
 
    sorted_low_nums = mergesort(low_nums, 0, mid)
    sorted_high_nums = mergesort(high_nums, 0, high - mid - 1 )
    return merge(sorted_low_nums, sorted_high_nums, mid + 1, high - mid  )


nums = [4, 8, 10, 1, 5, 9, 7]
res = mergesort(nums, 0, len(nums) - 1)
print(res)
