class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m_sum=0
        

        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i] < prices[j]:
                    m_sum = prices[j]
                    return m_sum
                    
        return m_sum

                
                

        
            