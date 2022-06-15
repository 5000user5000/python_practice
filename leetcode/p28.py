class Solution:
    
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        d = 29
        #q = math.pow(2,32) py3沒有極限
        if(length==0):
            return 0
        else:
            pattern = int(Solution.hashed(needle))
            inx = 0
            end = int(len(haystack)-len(needle))
            text = Solution.hashed(haystack[0:length])
            while(inx<end):
                if(pattern==text):
                    return inx
                text =  (text - int(math.pow(d,length-1))*(ord(haystack[inx])-96))*d + ord(haystack[inx+length] )-96 
                inx +=1
                
            if(pattern==text):
                    return inx  
            return -1
    def hashed(word):
        value = 0
        d = 29
        #q = math.pow(2,32)
        for i in word:
            value = int(value*d) #%q
            value += (ord(i)-96)
        return value
          
    
            
         
        
        
