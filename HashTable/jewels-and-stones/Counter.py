class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones)
        print(freqs)
        
        count = 0
        for char in jewels:
            count += freqs[char]
        
        return count
