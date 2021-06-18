array = [1,2,3]

def getAllPossibleArrays(array):
    permutations = []
    permutationHelper(0, array, permutations)
    return permutations

def permutationHelper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            permutationHelper(i+1, array, permutations)
            swap(array, i, j)

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

print(getAllPossibleArrays(array))