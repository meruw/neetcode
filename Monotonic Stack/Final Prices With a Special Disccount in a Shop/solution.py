class Solution:
    def discounts2(self,prices):
        stack = []

        for i in range(len(prices)):

            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop() #index to be written
                prices[j] = prices[j] - prices[i] #waiting for discount - applied discount

            stack.append(i) # queremos conservar el indice actual
        return prices






s = Solution()
print(s.discounts2([8,4,6,2,3]))
