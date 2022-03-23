"""
We consider alphabet with only three letters: "a", "b" and "c". A string is called diverse if no three consecutive letters are the same. In other words, a diverse string may not contain any of the strings "aaa", "bbb" or "ccc".
"""

# def solution(a,b,c):
#     # largest = max(a, max(b, c))

#     res = []
#     cntA, cntB, cntC = 0, 0, 0 # used to count the occurrences of corresponding character 
    
#     for i in range(a+b+c):
#         maxCount = max(a, b, c)
#         if (a == maxCount and cntA < 2) or (cntB == 2 and a >= 1) or (cntC == 2 and a >= 1):
#             res.append('a')
#             a = a-1
#             cntA = cntA+1
#             cntB, cntC = 0, 0
#         elif (b == maxCount and cntB < 2) or (cntA == 2 and b >= 1) or (cntC == 2 and b >= 1):
#             res.append('b')
#             b = b-1
#             cntB = cntB+1
#             cntA, cntC = 0, 0
#         elif (c == maxCount and cntC < 2) or (cntA == 2 and c >= 1) or (cntB == 2 and c >= 1):
#             res.append('c')
#             c = c-1
#             cntC = cntC+1
#             cntA, cntB = 0, 0
#     # end loop

#     return "".join(res)

# print(solution(1, 2, 3))


# use
def solution(A, B, C):
        total = A+B+C
        a=b=c=0
        res = ""
        while total > 0:
            if (A>=B and A>=C and a!=2) or (A>0 and (b==2 or c==2)):
                res +="a"
                a+=1
                b=c=0
                A-=1
            
            elif (B>=A and B>=C and b!=2) or (B>0 and (a==2 or c==2)):
                res +="b"
                b+=1
                a=c=0
                B-=1
            
            elif (C>=B and C>=A and c!=2) or (C>0 and (b==2 or a==2)):
                res +="c"
                c+=1
                a=b=0
                C-=1
            total -=1
            
        return res

print(solution(1, 2, 3))


from queue import PriorityQueue
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        q = PriorityQueue()
        q.put((-1*a,"a")) if a else None
        q.put((-1*b,"b")) if b else None
        q.put((-1*c,"c")) if c else None
        res = [] # We will append each letter in this list
        prev1 = "" 
        prev2 = ""
        while not q.empty():
            num, let = q.get()
            
            # choose next best letter, when the chosen letter appears third time
            if prev1 == let and prev1 == prev2 :
                if q.empty():
                    break
                tnum, tlet = q.get()          
                q.put((num,let))
                num = tnum
                let = tlet
                              
            num = -1*num            
            res.append(let)
            num=num-1
            
            # if still there is scope for adding letter, put back into PriorityQueue
            if num>0:
                q.put((-1*num,let))
            prev2=prev1
            prev1=let
                
        return "".join(res)
