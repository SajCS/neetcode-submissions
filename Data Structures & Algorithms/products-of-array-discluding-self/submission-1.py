class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        pre = []
        post = []
        counter = 1
        for i in nums:
            counter = counter*i
            pre.append(counter)
        counter = 1
        for i in nums[::-1]:
            counter = counter * i
            post.append(counter)
        post = post[::-1]
        print(pre, post)
        
        res = []

        for i in range(len(nums)):
            if i == 0:
                res.append(post[i+1])
            elif i == len(nums)-1:
                res.append(pre[i-1])
            else:
                print(nums[i], post[i+1], pre[i-1])
                res.append(post[i+1]*pre[i-1])
        return res


        