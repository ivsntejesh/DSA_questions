#array = [1,2,3, [4,[5]], 9, [2,3]]
array = [5,2, [7, -1], 3, [6, [-13, 8], 4]]

def prodsum(array, multiplier=1):
    s = 0

    for i in array:
        if (type(i) is list):
            r = prodsum(i, multiplier+1)
            s = s + r
        else:
            s = s + i

    return(s*multiplier)

print(prodsum(array))