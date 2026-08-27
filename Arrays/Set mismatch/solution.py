
class SetMismatch:
    def FixMismatch(self, s: list[int]) -> list[int]:
        numbers: list[int] = [0] * len(s)
        ans: list[int] = []
        current: int = 0
        count: int = 0
        duplicate: int = 0
        missing: int = 0

        for i in range(len(s)):
            current = s[i]
            count = 0
            for number in s:
                if(number == current):
                    count += 1

            if(count == 2 and current not in ans):
                duplicate = current
                ans.append(duplicate)
                count = 0

        for i in range(len(numbers)):
            i = i + 1
            count = 0
            for number in s:
                if(i == number):
                    count += 1

            if(count == 0):
                missing = i
                ans.append(missing)
        return ans

class SolutionProTry:
    def FixMismatch(self, numbers: list[int]) -> list[int]:
        nList: list[int] = [0] * len(numbers)
        duplicate: int = 0
        missing: int = 0
        count: int = 0
        current: int = 0
        currentValue: int = 0


        for i in range(len(numbers)):
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("New cycle")
            count = 0
            current = i + 1
            currentValue = numbers[i]
            print("current index")
            print(current)
            print("current value")
            print(currentValue)
            print("Current array")
            print(nList)
            print ("Numbers array")
            print(numbers)
            for number in numbers:
                print("======================")
                print("Passed values:")
                print("current")
                print(current)
                print("Current number in numbers")
                print(number)
                if(current == number):
                    print("=================================")
                    print("current == number")
                    print(current)
                    print("=")
                    print(number)
                    count +=1
                    print("count")
                    print(count)
                    nList[i] = count
                    print(nList)

                if(count == 2):
                    nList[i] = count
        print(nList)

        for i in range(len(nList)):
            current = i + 1
            if(nList[i] == 2):
                duplicate = current
            if(nList[i] == 0):
                missing = current

        return [duplicate, missing]


class SolutionProDefinitiva:
    def FixMismatch(self, numbers: list[int]) -> list[int]:
        missing: int = 0
        duplicate: int = 0
        nList: list[int] = [0] * len(numbers)

        #if n = 4 then [1,2,3,4]
        # numbers go from 1,2,3 or 4
        # nlist with len(numbers) will have 4 indexes
        # indexes start from 0
        # since numbers go from 1-4, then number - 1 will always match an index on nList
        # with that:
        # number = 3
        # 3-1 = 2
        # nlist index 2 will add 1
        # [0,0,1,0]
        # if 3 repeats again
        # [0,0,2,0]
        # if single number, will only add 1 to nlist[number -1]
        # if no number on numbers array, then said index will remain at 0
        for number in numbers:
            nList[number - 1] += 1 # you can add numbers to a specific index on an int list

        for i in range(len(nList)):
            if (nList[i] == 2):
                duplicate = i + 1
            if(nList[i] == 0):
                missing = i + 1

        return [duplicate, missing]


s = SolutionProDefinitiva()
print(s.FixMismatch([1,1,2,3]))
