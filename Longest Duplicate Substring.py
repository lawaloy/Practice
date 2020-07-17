class Solution(object):
    def longestDupSubstring(self, S):
        """
        :type S: str
        :rtype: str
        """
        p = 2**63-1
        def rabin_karp(mid):
            cur_hash = 0
            for i in range(mid):
                cur_hash = (cur_hash * 26 + nums[i]) % p
            hashes = {cur_hash}
            pos = -1
            max_pow = pow(26, mid, p)
            for i in range(mid, len(S)):
                cur_hash = (26 * cur_hash - nums[i - mid]*max_pow + nums[i]) % p
                if cur_hash in hashes:
                    pos = i + 1 - mid
                hashes.add(cur_hash)
            return pos
        
        
        #BST
        nums = [ord(c) for c in S]
        left, right = 0, len(S)-1
        start, end = 0,0
        while left <= right:
            mid = left + (right - left)//2
            pos = rabin_karp(mid)
            if pos == -1:
                right = mid-1
            else:
                start,end = pos, pos + mid
                left = mid+1
                
        return S[start:start+left -1]
