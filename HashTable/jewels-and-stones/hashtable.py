class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = {}
        for char in stones:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
        
        print(freq)
        
        count = 0
        for char in jewels:
            if char in freq:
                count += freq[char]
        
        return count
