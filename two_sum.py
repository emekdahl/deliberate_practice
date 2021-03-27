def twoSum(self, nums: List[int], target: int) -> List[int]:
    for index, num in enumerate(nums):
        for ndex, digit in enumerate(nums):
            if index != ndex:
                if num + digit == target:
                    return [index, ndex]
