class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_of_all = 1
        result= []
        zero_count = nums.count(0)
        
        if zero_count == 0:
            for i in nums:
                product_of_all *= i
        elif zero_count == 1:
            for i in nums:
                if i != 0:
                    product_of_all *= i
        elif zero_count > 1:
            product_of_all = 0
        
        print(product_of_all)
        
        for i in nums:
            if zero_count == 0:
                result.append(int(product_of_all / i))
            elif zero_count == 1:
                if i == 0:
                    result.append(product_of_all)
                else:
                    result.append(0)
            elif zero_count > 1:
                result.append(0)
        
        return result