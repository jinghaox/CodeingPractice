def max_sub_array(arr):
    max_sum = 0
    cur_sum = 0
    # starting position of the max_sub_array
    start = 0
    # ending position of the max_sub_array
    end = 0

    # updated start position of the max_sub_array
    updated_start = 0

    i = 0
    while i < len(arr):
        cur_sum += arr[i]
        if cur_sum < 0:
            # this means we will restart counting from next value
            updated_start = i+1
            cur_sum = 0
        else:
            if cur_sum > max_sum:
                # only update start when cur_sum>max_sum, if not, which means the previous max_sum is still valid
                # so we don't need to update the start position
                start = updated_start 
                max_sum = cur_sum
                # update ending position
                end = i
        i += 1
    
    sum_range = [start, end]
    return sum_range, max_sum
        
def kadanesAlgorithm(array):
    maxEndingHere = array[0] 
    maxSoFar = array[0] 
    print("maxEndinghere, maxSoFar")
    for i in range(1, len(array)):
        num = array[i]
        maxEndingHere = max(num, maxEndingHere + num)
        # if maxEndingHere is <0, then maxEndingHere + num < num, then we restart calculating maxsum from this num 
        # otherwise, if maxEndingHere is >=0, then maxEndingHere+num >= num, we still use 
        maxSoFar = max(maxSoFar, maxEndingHere)
        print(maxEndingHere, "\t", maxSoFar)
    return maxSoFar

arr = [-1,2,3,4,-5,6,-2,7] 
sum_range, max_sum = max_sub_array(arr)
print(max_sum)
print("The max sub array is within {}".format(sum_range))
print(arr[sum_range[0]:sum_range[1]+1])
print(sum(arr[sum_range[0]:sum_range[1]+1]) == max_sum)

max_sum = kadanesAlgorithm(arr)
print(max_sum)
