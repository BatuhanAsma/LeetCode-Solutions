class Solution(object):
    def romanToInt(self,s):
            alphabet_list=["I",1,"V",5,"X",10,"L",50,"C",100,"D",500,"M",1000]
            t=0
            r=0
            for i in s:
                if (s[r]=="I" and r!=len(s)-1) and ( s[r+1]=="V" or s[r+1]=="X"):
                    t = t- alphabet_list[alphabet_list.index(i)+1]
                elif (s[r]=="X" and r!=len(s)-1) and ( s[r+1]=="L" or s[r+1]=="C"):
                    t = t- alphabet_list[alphabet_list.index(i)+1]
                elif (s[r]=="C" and r!=len(s)-1) and ( s[r+1]=="D" or s[r+1]=="M"):
                    t = t- alphabet_list[alphabet_list.index(i)+1]
                else:
                    t = t+alphabet_list[alphabet_list.index(i)+1]
                r=r+1
            return t