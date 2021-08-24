---
title: Interesting Hard Questions
layout: post
categories: 
  - blog
tags:
  - leetcode summary
---



## Interesting Hard Questions:

1. Median of two sorted arrays:

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

 

**Example 1:**

```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

**Example 2:**

```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

**Example 3:**

```
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
```

**Example 4:**

```
Input: nums1 = [], nums2 = [1]
Output: 1.00000
```

**Example 5:**

```
Input: nums1 = [2], nums2 = []
Output: 2.00000
```

 

**Constraints:**

- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-106 <= nums1[i], nums2[i] <= 106`



### Solution:

1. 如果brute force 我们直接 merge，得到median就 O(m+n). 看到题目要求 O(log(m+n)), 知道应该使用 binary search. 
2. **考虑，如果我们在 array A 中找到一个index i，在 array B 中对应的 index j（median或median旁边），必须满足 i + j = (m + n + 1)/2. 而且，必须满足 A[i-1] < B[j] 且 B[j-1] < A[i]。**
3. 如果 A[i-1] > B[j], 证明说 A[i] 会比真正 median 大，所以 i 减小；反之亦然。

总结起来就是这个图片：

{% asset_img image fit 1_exp.png %}



结合以上的点，我们选择在 array A 里面搜索，然后找到 对应的 array B 中的 index j, 之后接着判断。 

> 这里我们因为 j = (m+n+1)/2 - i 得到，**保证 j >= 0, 所以需要 m <= n。**而且也加快搜索速度！！！

```python
def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        # if n == 0:
        #     raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])
                    
                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0
```

**注意这里 i 的搜索范围是 [0,m], 因为 i 类似于 cut，i=0 代表 A[0] 也在 right_part, i=m 代表 A[m-1] 在 left_part**

因为 (m+n+1)/2 保证了左边比右边长，所以如果奇数的话，max_of_left 就是 median



---



2. Trapping Rain Water

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

**Example 2:**

```
Input: height = [4,2,0,3,2,5]
Output: 9
```

 

**Constraints:**

- `n == height.length`
- `1 <= n <= 2 * 104`
- `0 <= height[i] <= 105`



### Solution:

1. 先考虑 brute-force, 对于每一个点，我们考虑左边的最高的墙和右边的最高的墙，最终能hold的水为 min(left_height, right_height) - curr_height. 这样就 O(n^2)/O(1)

2. Brute-force 基础上我们用 **DP** 存下左边到右边的高度，和右边到左边的高度，之后直接求. O(n)/O(n)

3. 用一个 stack 来做，观察到如果有 valley，我们会去iterate直到比当前 height 高的时候，这个时候我们更新得到的water，同时把这个valley弄平掉。O(n)/O(n), faster than 2., in one pass.

   1. 我们往 stack 中添加 index，如果比当前 index 的 height 低，则继续添加；如果比 top() 的 height 大，证明出现了valley，pop 出小的部分，计算得到的水量计入总量；

   ```c++
   int trap(vector<int>& height)
   {
       int ans = 0, current = 0;
       stack<int> st;
       while (current < height.size()) {
           while (!st.empty() && height[current] > height[st.top()]) {
               int top = st.top();
               st.pop();
               if (st.empty())
                   break;
               int distance = current - st.top() - 1;
               int bounded_height = min(height[current], height[st.top()]) - height[top];
               ans += distance * bounded_height;
           }
           st.push(current++);
       }
       return ans;
   }
   ```

4. **two pointers approach: O(n)/O(1)**

Best explained here:

{% youtuber video XqTBrQYYUcc %}
{% endyoutuber %}

总结就是：

1. 我们对于每个 index 都在求函数 g(i) = min(left_max(i), right_max(i) )。这个类似于求 lower envelop, **遇到类似lower envelop问题就是要想到 two pointers 或者 binary search**，这里介绍 two pointers 办法

2. 利用 left_max 函数 non-decreasing 和 right_max 函数 non-increasing 的性质，每次对比决定 pointer i 还是 pointer j 往中间移动。

```java
class Solution {
    public int trap(int[] height) {
        // time : O(n)
        // space : O(1)
        if (height.length==0) return 0; 
        int left = 0, right = height.length-1; 
        int leftMax=0, rightMax=0; 
        int ans = 0; 
        while (left < right) {
            if (height[left] > leftMax) leftMax = height[left]; 
            if (height[right] > rightMax) rightMax = height[right];
            if (leftMax < rightMax) {
                ans += Math.max(0, leftMax-height[left]); 
                left++; 
            } else {
                ans += Math.max(0, rightMax-height[right]); 
                right--; 
            }
        }
        return ans; 
    }
}
```



---



