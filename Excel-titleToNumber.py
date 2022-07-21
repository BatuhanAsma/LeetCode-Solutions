class Solution(object):
    def titleToNumber(self, columnTitle):
        a = columnTitle.replace('columnTitle','')
        b= a.strip('= " "')
        y=[chr(i) for i in range(ord('A'),ord('Z')+1)]
        rtype=0
        counter=0
        for i in b:
            rtype = rtype + len(y)**(len(b)-(counter+1))*(y.index(i)+1)
            counter+=1
        print(y)
        print(rtype)
        return rtype
    
