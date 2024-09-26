class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck)<2:
            return False
        
        seen_dict={}
        for each in deck:
            if each in seen_dict:
                seen_dict[each]=seen_dict[each]+1
            else:
                seen_dict[each]=1
        
        temp=[i for i in seen_dict.values()]
        print(temp)
        return True if reduce(math.gcd, temp)>1 else  False 

  

        