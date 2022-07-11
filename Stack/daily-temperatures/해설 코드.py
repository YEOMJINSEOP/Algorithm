class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        
        for i, cur in enumerate(temperatures):
            print("cycle", (i + 1))
            print("i = ", i, "," "cur = ", cur)
            while stack and cur > temperatures[stack[-1]]: #stack이 empty면 while stack에서 false
                last = stack.pop()
                print("popped => ", last)
                answer[last] = i - last
            stack.append(i)
            print("stack : ", stack)
            print("answer :", answer, " \n")
