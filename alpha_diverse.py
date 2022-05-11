"""
We consider alphabet with only three letters: "a", "b" and "c". A string is called diverse if no three consecutive letters are the same. In other words, a diverse string may not contain any of the strings "aaa", "bbb" or "ccc".
"""

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


# from queue import PriorityQueue
# class Solution:
#     def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
#         q = PriorityQueue()
#         q.put((-1*a,"a")) if a else None
#         q.put((-1*b,"b")) if b else None
#         q.put((-1*c,"c")) if c else None
#         res = [] # We will append each letter in this list
#         prev1 = "" 
#         prev2 = ""
#         while not q.empty():
#             num, let = q.get()
            
#             # choose next best letter, when the chosen letter appears third time
#             if prev1 == let and prev1 == prev2 :
#                 if q.empty():
#                     break
#                 tnum, tlet = q.get()          
#                 q.put((num,let))
#                 num = tnum
#                 let = tlet
                              
#             num = -1*num            
#             res.append(let)
#             num=num-1
            
#             # if still there is scope for adding letter, put back into PriorityQueue
#             if num>0:
#                 q.put((-1*num,let))
#             prev2=prev1
#             prev1=let
                
#         return "".join(res)
