# 暴力解
class Solution:
    def fizzBuzz(self, n):
        ans = []

        for num in range(1,n+1):
            if num % 3 == 0 and num % 5 == 0:
                ans.append("FizzBuzz")
            elif num % 3 == 0:
                ans.append("Fizz")
            elif num % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(num))

        return ans

# string
class Solution:
    def fizzBuzz(self, n):
        ans = []

        for num in range(1,n+1):

            s = ""

            if num % 3 == 0:
                s += "Fizz"
            if num % 5 == 0:
                s += "Buzz"
            if not num_ans_str:
                s = str(num)

            ans.append(s)  

        return ans

# hashing
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        hashtable = {3:"Fizz", 5:"Buzz"}
        ans = []
        for i in range(1,n+1):
            element = ""
            for k in hashtable.keys():
                if i % k == 0:
                    element+=hashtable[k]
            if element == "":
                element = str(i)
            ans.append(element)
        return ans