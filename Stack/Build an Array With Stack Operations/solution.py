class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        output: list[str] = []
        j : int = 0
        for x in range(1, n+1):
            print(f"j: {j}")
            if(x != target[j]):
                print(f"Evaluated: if {x} != {target[j]}")
                print("Push,Pop")
                output.append("Push")
                output.append("Pop")
            else:
                print(f"Evaluated: if {x} == {target[j]}")
                print("Push only")
                output.append("Push")
                j+= 1
            if(j == len(target)):
                return output





s = Solution()
print(s.buildArray([1,3,5],5))
