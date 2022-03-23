"""
Given an integer N(1 < N < 100) returns an array containing N unique integers that sum up to 0.Th function can return any such aray.

"""

# def solution(N):
#     ans =[]

#     if N >= 1 and N <= 1000:
#         for i in range(1, N//2 + 1):
#             ans.append(1)
#             ans.append(-1)

#         if N % 2 != 0:
#             ans.append(0)
#     return ans

# print(solution(4))

# def solution(N):
#     ans = []
#     pos = 1
#     quotient = N//2 + 1

#     while pos < quotient:
#         ans.append(1)
#         ans.append(-1)
#         pos += 1

#     if N % 2 != 0: ans.append(0)s
#     return ans        
 
# print(solution(3))

# def solution(n):
#     s = []
#     for i in range(1,n+1) :
#         s.append(i)
#     s[-1] = (sum(s[0:len(s)-1]))*-1
#     return s

# print(solution(4))

# def solution(n):
#         m=n
#         if n%2!=0:
#             n-=1
#         z=[]
#         l=1
#         while len(z)!=n and n%2==0:
#             z.append(l)
#             z.append(-l)
#             l+=1
#         if m%2==0: return z
#         else: return z+[0]
# print(solution(9))

def solution(n):
        answer = []
        
        for i in range(1, n // 2 + 1):
            answer.append(i)
            answer.append(-i)
        
        if len(answer) < n:
            answer.append(0)
        
        return answer

print(solution(9))
