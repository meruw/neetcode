class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        t: int = 0
        currentStart: int = 0
        addedTime: int = 0
        currentExecuting: int = 0
        functions = {}
        status = {"start", "end"}
        callStack: list[int] = []


        for x in logs:
            parts = x.split(":")

            if int(parts[0]) not in functions:

                functions[int(parts[0])] = 0

            if(parts[1] == "start"):
                print(f"Evaluating: {x}")
                print("start initiated")
                t = int(parts[2])
                print(f"new t value: {t}")
                if len(callStack) > 0:
                    print("There was a function in stack, adding time value")
                    addedTime = t - currentStart
                    print(f"new addedTime value comes from: {t} - {currentStart}")
                    currentExecuting = callStack[len(callStack) - 1] # last one on stack is the one currently executing
                    functions[currentExecuting] += addedTime
                    print(f"New functions array after summing {addedTime} to {functions[currentExecuting]} key")
                currentStart = t
                callStack.append(int(parts[0]))
                print(f"Current callStack: {callStack}")
                print(f"Current functions: {functions}")


            if(parts[1] == "end"):
                print(f"end initiated")
                t = int(parts[2]) + 1
                print(f"new t value: {t}")
                addedTime = t - currentStart
                print(f"new addedTime value comes from: {t} - {currentStart}")
                currentExecuting = callStack[len(callStack) - 1]
                functions[currentExecuting] += addedTime
                print(f"New functions array after summing {addedTime} to {functions[currentExecuting]} key")
                callStack.pop() #whichever is running when log has end has to be the one at the top
                currentStart = t
                print(f"Current callStack: {callStack}")
                print(f"Current functions: {functions}")

        output = []

        for i in range(n):
            output.append(functions[i])

        return output

    #n is number of functions




s = Solution()
print(s.exclusiveTime(2,["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]))
