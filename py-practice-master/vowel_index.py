def capitals(word):
    #your code here
    indexArray = []
    for index, char in enumerate(word):
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            indexArray.append(index)

    return indexArray

capitals('CodEWaRs')