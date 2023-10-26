def solution1(nums):
    nums_set = set(nums)
    return len(nums_set) if len(nums_set) < len(nums)/2 else len(nums)//2

def solution2(nums):
    pocketmons = {}
    for num in nums:
        if pocketmons.get(num) == None:
            pocketmons[num] = 0
        pocketmons[num] = pocketmons[num]+1
    return len(pocketmons.keys()) if len(pocketmons.keys()) < len(nums)/2 else len(nums)//2