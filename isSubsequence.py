class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c1 = 0
        c2 = 0
        l1 = len(s)
        l2 = len(t)

        if s == "":
            return True
        
        if l1 > l2:
            return False

        if l1 == l2:
            if s != t:
                return False
            else:
                return True


        while True:
            #print ("start ",c1,c2, s[c1], t[c2], l1,l2)


            if s[c1] == t[c2]:
                c2 += 1
                c1 += 1
            else:
                c2 += 1

  
            if c1 == l1:
                return True
            
            if c2 == l2:
                return False 

            #print ("end ",c1,c2, s[c1], t[c2])
