class Solution(object):
    def judgeCircle(self, moves):
        sumx=0
        sumy=0
        for i in moves:
            if(i == 'R'):
                sumx+=1
            elif(i=='L'):
                sumx-=1
            elif(i=='U'):
                sumy+=1
            elif(i=='D'):
                sumy-=1
        if (sumx==0 and sumy==0):
            return True
        else:
            return False