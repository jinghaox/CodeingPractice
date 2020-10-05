# this algorithm shifts two arrays
# not working
# e.g. this is ok
#  abcx
# xabc
# but this is not working (same chars are abc & ef, total 5 chars)
# shifting only gets abc (total 3 chars)
#   abcxeft
#   abcefg
def find_lv_dist(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2)

    if len1 < len2:
        arr1, arr2 = arr2, arr1
        len1, len2 = len2, len1

    max_dist = 0
    for i in range(0, len2):
        # left shift
        s1 = arr1[0:len2-i]
        s2 = arr2[i:len2]
        dist = 0
        for j in range(len(s2)):
            if s1[j] == s2[j]:
                dist += 1
        if max_dist <= dist:
            max_dist = dist
            print("max_dist = {}".format(max_dist))
            print("s1 = {}".format(s1))
            print("s2 = {}".format(s2))
            left = i
            mid = len(s1) - max_dist
            right = len1-(len2-i)
            operations = left + mid + right
    
    left_shift_steps = operations
    print(operations)
        
    print("-"*20)
    for i in range(0, len2):
        # right shift
        min_len = min(len1-i, len2)
        s1 = arr1[i:i+min_len]
        s2 = arr2[len2-min_len:len2]
        dist = 0
        for j in range(len(s2)):
            if s1[j] == s2[j]:
                dist += 1
        if max_dist <= dist:
            max_dist = dist
            print("max_dist = {}".format(max_dist))
            print("s1 = {}".format(s1))
            print("s2 = {}".format(s2))
            left = i
            mid = len(s1)-max_dist
            right = len1-(i+min_len)
            operations = left + mid + right

    right_shift_steps = operations
    steps = min(left_shift_steps, right_shift_steps)

    return(max_dist, steps)

arr1 = "algoexpert"
arr2 = "algozexpert"
dist, oper = find_lv_dist(arr1, arr2)
print("distance = {}".format(dist))
print("steps = {}".format(oper))


