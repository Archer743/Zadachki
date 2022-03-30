def fibonacci(nums : int):
    if nums < 0: return None
    elif nums == 1: return [0]
    elif nums == 2: return [0, 1]
    else:
        l = [0, 1]
        for i in range(2, nums):
            l.append(l[len(l)-1] + l[len(l)-2])
        return l

def recFibonacci(nums : int, l : list = [0, 1]):
    if len(l) == 2 and nums == 1:  # ако има 2 числа в листа и искаме само едно число
        return [0]
    elif len(l) == 2 and nums == 2:  # ако има 2 числа в листа и искаме само две числа
        return [0, 1]
    elif len(l) < 2 or nums <= 0:  # ако имаме по-малко от 2 елемента в листа или чилсото ни е по-малко или равно на 0
        return None
    elif len(l) == nums:  # ако имаме толкова числа в масива, колкото иска user-а
        return l
    else:
        l.append(l[len(l)-1] + l[len(l)-2])
        return recFibonacci(nums, l)


if __name__ == "__main__":
    numsGenerated = int(input("How many Fibonnaci numbers to be generated: "))
    print(f"Normal: {fibonacci(numsGenerated)}")
    print(f"Recursive: {recFibonacci(numsGenerated)}")