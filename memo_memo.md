#### 5. Longest Palindromic Substring
<details>
<summary>See Memo</summary>

* dp[i][j]
* start building dp from the end
  
</details>

#### 18. 4Sum
<details>
<summary>See Memo</summary>

* sort array in order to remove duplicates
* Initial check
```python
if len(nums) < k or nums[0] * k > target or nums[-1] * k < target:
    return []
```

* Skip duplicates in while loop
```python
# twoSum
while lo < hi:
	...
	if sum < target or (lo > start and nums[lo - 1] == nums[lo]):
	...
	elif sum > target or (hi < len(nums) - 1 and nums[hi + 1] == nums[hi]):
	...
```

* Be careful with looping from start

</details>

#### 23. Merge k Sorted Lists
<details>
<summary>See Memo</summary>

* Use heapq (ListNode must be comparable, need to define __lt__ and __le__)
* Use divide and conquer
```python
interval = 1
while interval < k:
    for i in range(0, k - interval, interval * 2):
        lists[i] = self.merge2Lists(lists[i], lists[i + interval])
    interval *= 2
```

</details>

#### 31. Next Permutation
<details>
<summary>See Memo</summary>

* Starting from right, the first number that is smaller than its succeeding number is the one that needs to be changed
* Find the least bigger number from the right, swap them
* Reverse the rest

</details>

#### 41. First Missing Positive
<details>
<summary>See Memo</summary>

* Smallest possible missing positive is 1
* Solution must be in [1, N + 1], so mark all impossible values as 1
* Calculate corresponding index for each num and mark negative if it exists
```python
for i in range(len(nums)):
	index = abs(nums[i]) - 1
	if index < len(nums) and nums[index] > 0:
		nums[index] = -nums[index]
```
* Loop through and find first positive, its index is the first missing positive

</details>

#### <Template>
<details>
<summary>See Memo</summary>

</details>
