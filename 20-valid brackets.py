class Solution:
    def isValid(self, s: str) -> bool:
      map_dic={")":"(","]":"[","}":"{"}
      stack=[]
      for p in s:
          if p in map_dic:
             if len(stack)>0 and map_dic[p]==stack[-1]:
                 stack.pop()
             else:
                 return False
          else:
              stack.append(p)
      return not stack 

s=Solution()
print(s.isValid("()"))