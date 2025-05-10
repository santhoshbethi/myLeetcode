class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter=Counter(s1)
        s_count=Counter()
        for i in range(len(s2)):
        # Add current character
            s_count[s2[i]] += 1
            
            # Remove character outside the window
            if i >= len(s1):
                if s_count[s2[i - len(s1)]] == 1:
                    del s_count[s2[i - len(s1)]]
                else:
                    s_count[s2[i - len(s1)]] -= 1
            if s1_counter == s_count:
                return True
        return False
                


                



        