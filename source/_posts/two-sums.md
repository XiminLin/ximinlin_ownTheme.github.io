---
title: Two Sums
layout: post
categories: 
  - blog
tags:
  - leetcode summary
---

Leetcode summary from 2Sums and its modification to NSums.
<!-- more -->

## Two Sums:

```
Two sums:

 	1. sort + two pointers
 	2. hashmap for equal question

N-sums:

1. 分解成 n-1 sums，像 3sums 变 2sums, 之后 pointers 里面找规律能不能 O(n) 来做
```



1. Two Sums

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have ***exactly\* one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

 

**Example 1:**

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

 

**Constraints:**

- `2 <= nums.length <= 104`
- `-109 <= nums[i] <= 109`
- `-109 <= target <= 109`
- **Only one valid answer exists.**



### Solution:

Best solution: O(n)/O(n), hashmap that checks if one's complement is in the hashset, if not keep inserting, otherwise return.



---



2. Two Sums II

Sorted in non-descending order array, find two numbers that add up to target.



### Solution:

Best solution: O(n)/O(1), two pointers, index i from 0, index j from len-1. i controls increasing the current sum. j controls decreasing the current sum.



---



3. Two Sums III:



Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

Implement the `TwoSum` class:

- `TwoSum()` Initializes the `TwoSum` object, with an empty array initially.
- `void add(int number)` Adds `number` to the data structure.
- `boolean find(int value)` Returns `true` if there exists any pair of numbers whose sum is equal to `value`, otherwise, it returns `false`.



### Solution:

Hashset the keeps appending O(n)/O(n).



---



4. Two Sums IV:

Given the `root` of a Binary Search Tree and a target number `k`, return *`true` if there exist two elements in the BST such that their sum is equal to the given target*.

 

**Example 1:**

```
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
```

**Example 2:**

```
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
```

**Example 3:**

```
Input: root = [2,1,3], k = 4
Output: true
```

**Example 4:**

```
Input: root = [2,1,3], k = 1
Output: false
```

**Example 5:**

```
Input: root = [2,1,3], k = 3
Output: true
```

 

**Constraints:**

- The number of nodes in the tree is in the range `[1, 104]`.
- `-104 <= Node.val <= 104`
- `root` is guaranteed to be a **valid** binary search tree.
- `-105 <= k <= 105`



### Solution:

preorder traverse 一下，得到 ordered set，可以用 hashset 来做，或者 two pointers 来做. O(n)/O(n)



---



5. **3Sum**

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.



### Solution:

1. two pointers: O(n^2)/O(n), sort 之后, index i fom 0 to len-3. index j 和 index k 在 右侧找 complement。



2. Hashset: O(n^2)/O(n), i 从左到右，j 对于右边剩下的部分做 hashset 2Sums，对于避免duplicates：

   1. NoSort:
      1. 对于确定 i:
         1. j 那里是不会有 dup 的，直接用 two-pass hashset 即可
      2. 多保存一个 hashset 来表示已经看过的 nums[i] 值即可，如果又出现 nums[i] 直接跳过

   2. Sort:
      1. 如果 nums[i-1] == nums[i], 跳过 i，就能保证 no dup



**Hashset trick: 在确定 i 的时候，每次都要重新插入 hashset，不如我们做一次 hashmap, 后面每次 i 增加，都把 hashmap 里面的 i 给标记成 invalid，之后寻找的时候就看看 complement 是不是 invalid 的，只是一个 trick，能加快 c++ 一倍的速度**

```c++
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> res;
        unordered_set<int> dups;
        unordered_map<int, int> seen;
        for (int i = 0; i < nums.size(); ++i)
            if (dups.insert(nums[i]).second) {
                for (int j = i + 1; j < nums.size(); ++j) {
                    int complement = -nums[i] - nums[j];
                    auto it = seen.find(complement);
                    if (it != end(seen) && it->second == i) {
                        vector<int> triplet = {nums[i], nums[j], complement};
                        sort(begin(triplet), end(triplet));
                        res.insert(triplet);
                    }
                    seen[nums[j]] = i;
                }
            }
        return vector<vector<int>>(begin(res), end(res));
    }
};
```



---



6. Two Sums less than k

   Given an array `nums` of integers and integer `k`, return the maximum `sum` such that there exists `i < j` with `nums[i] + nums[j] = sum` and `sum < k`. If no `i`, `j` exist satisfying this equation, return `-1`.

    

   **Example 1:**

   ```
   Input: nums = [34,23,1,24,75,33,54,8], k = 60
   Output: 58
   Explanation: We can use 34 and 24 to sum 58 which is less than 60.
   ```

   **Example 2:**

   ```
   Input: nums = [10,20,30], k = 15
   Output: -1
   Explanation: In this case it is not possible to get a pair sum less that 15.
   ```

    

   **Constraints:**

   - `1 <= nums.length <= 100`
   - `1 <= nums[i] <= 1000`
   - `1 <= k <= 2000`



### Solution:

1. O(nlogn)/O(1), sort 之后 two pointers, 我们需要不停的向 k 逼近，i+j >= k 时，j--; i+j < k 时 i++; 知道 i == j 退出，找到max
2. O(m+n)/O(m), 假设 数组包含了 m 个 unique values（constraints 说明了 **m<=1000** ），假设 n >> m 的时候，这种方法就好用了，把 0...1000 当做数组，lo = 0, hi = 1000.
   1. count array 记录所有出现的 number 的次数
   2. 全部 lo <= hi (因为可能存在 dup numbers in array)
   3. lo + hi >= k 或 count[k] == 0: hi --
   4. lo + hi < k, 如果 lo == hi 则check count[lo] >= 2; 则 存下来后面对比



---



7. 3Sum smaller

Given an array of `n` integers `nums` and an integer `target`, find the number of index triplets `i`, `j`, `k` with `0 <= i < j < k < n` that satisfy the condition `nums[i] + nums[j] + nums[k] < target`.

 

**Example 1:**

```
Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]
```

**Example 2:**

```
Input: nums = [], target = 0
Output: 0
```

**Example 3:**

```
Input: nums = [0], target = 0
Output: 0
```

 

**Constraints:**

- `n == nums.length`
- `0 <= n <= 3500`
- `-100 <= nums[i] <= 100`
- `-100 <= target <= 100`



### Solution:

1. two pointers, index triplets 这里只要求 index 不一样即可，而且只计算数量; O(n^2)/O(n)； O(n) space 是因为 sorting，但如果允许的话，就是 O(1)

   ```c++
   class Solution {
   public:
       // 想法就是 two pointers，i 从左到右，j=0,k=len-1，然后 k 不断从右逼近，把 i+j+k >= t 的都排除掉
       // 然后ok的话就 计算 k-j 则表示(j,j+1)...(j,k) 都满足条件，加到总数去
       // 之后 j+1, k 继续变小，直到 j==k 退出
       // O(n^2)/O(n)
       int threeSumSmaller(vector<int>& nums, int target) {
           int count = 0;
           sort(nums.begin(), nums.end() );
           int length = nums.size();
           for(int i = 0; i < length-2; i++) {
               int j = i+1, k = length-1;
               while(j < k) {
                   int sum = nums[i] + nums[j] + nums[k];
                   if(sum >= target) {
                       k--;
                   }
                   else{
                       count += k - j;
                       j++;
                   }
               }
           }
           return count;
       }
   };
   ```

   > 这里注意一点，nums.size() 返回是 size_t, 这里做 size_t-1 和 size_t-2 可能会overflow
   >
   > **所以最好是用 int length = ... 来间接的操作一下**



---



8. 3Sums closest

Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that the sum is closest to `target`.

Return *the sum of the three integers*.

You may assume that each input would have exactly one solution.

 

**Example 1:**

```
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```

**Example 2:**

```
Input: nums = [0,0,0], target = 1
Output: 0
```

 

**Constraints:**

- `3 <= nums.length <= 1000`
- `-1000 <= nums[i] <= 1000`
- `-104 <= target <= 104`



### Solution:

1. 3sums 变 2sums，sort 之后，如果 j+k > t, 则 j + {k+1} 会更大，则没有用，所以接着看 j + {k-1}. 另一个方向同理. O(n^2)/O(n); 

   

---



9. 4sums

Given an array `nums` of `n` integers, return *an array of all the **unique** quadruplets* `[nums[a], nums[b], nums[c], nums[d]]` such that:

- `0 <= a, b, c, d < n`
- `a`, `b`, `c`, and `d` are **distinct**.
- `nums[a] + nums[b] + nums[c] + nums[d] == target`

You may return the answer in **any order**.

 

**Example 1:**

```
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

**Example 2:**

```
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
```

 

**Constraints:**

- `1 <= nums.length <= 200`
- `-109 <= nums[i] <= 109`
- `-109 <= target <= 109`



### Solution:

1. 变成 3sums 接着做, O(n^3)/O(n)



---



10. 4Sums II

Given four integer arrays `nums1`, `nums2`, `nums3`, and `nums4` all of length `n`, return the number of tuples `(i, j, k, l)` such that:

- `0 <= i, j, k, l < n`
- `nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0`

 

**Example 1:**

```
Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
```

**Example 2:**

```
Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
```

 

**Constraints:**

- `n == nums1.length`
- `n == nums2.length`
- `n == nums3.length`
- `n == nums4.length`
- `1 <= n <= 200`
- `-228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228`



### Solution:

1. 这里思考因为不是同一个 vector，所以不能  two pointers, 但是因为是 equal 问题，我们用 hashset 可以，这里可以用 3个 forloop 来控制 i,j,k, 之后用 O(1) 的 hash 来找 l. 这样就是 O(n^3)/O(n)

2. **这里更好的方法是分成 两组，然后构建 i+j 的 hashset，和 k+l 的 hashset，之后对比两个hashset来找，这样就是 O(n^2)/O(n^2)**

   