def listRemoveDuplicatesOne(l : list):
    cpy = []
    for item in l:
        if item not in cpy: cpy.append(item)
    
    return cpy

def listRemoveDuplicatesTwo(l : list):
    l = list(set(l))
    return l


if __name__ == "__main__":
    l1 = [0, 1, 1, 3, 0]
    l2 = [4, 3, 3, 4, 6]

    print("First:", l1)
    l1 = listRemoveDuplicatesOne(l1)
    print("Result 1:", l1, "\n")

    print("Second:", l2)
    l2 = listRemoveDuplicatesTwo(l2)
    print("Result 2:", l2)