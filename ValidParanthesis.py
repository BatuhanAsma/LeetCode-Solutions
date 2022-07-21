class Solution(object):
    def isValid(self, s):
        self.s = s
        if len(s)%2!=0 or s[0]=="]" or s[0]==")" or s[0]=="}" :
            return False
        l1 = list()
        for i in s:
            if i=="(" or i=="[" or i=="{":
                l1.append(i)
            elif i==")" and len(l1)>1 and l1[-1]!="(":
                return False
            elif i=="]" and len(l1)>0 and l1[-1]!="[":
                return False
            elif i=="}"and len(l1)>0 and l1[-1]!="{":
                return False
            else:
                if len(l1)>0:
                    l1.pop(len(l1)-1)
                else:
                    return False
        if len(l1)!=0:
            return False
        else:
            return True
            
