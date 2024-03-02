"""131-partition
"""
class Solution:
    def partition(self,s):
        
        l,res=len(s),list()
        
        def dfs(start,tmp):
            if start>=l:
                res.append(tmp[:])
            for i in range(start,l):
                substring=s[start:i+1]
                if substring==substring[::-1]:
                    tmp.append(substring)
                    dfs(i+1,tmp)
                    tmp.pop()
        dfs(0,list())
        return res
if __name__ == "__main__":
    sol = Solution()
    input_str = "aabb"
    output = sol.partition(input_str)
    print("输入字符串:", input_str)
    print("分割方案:", output)
