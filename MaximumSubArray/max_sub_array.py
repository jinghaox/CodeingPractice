def max_sub_array(arr):
    max_sum = 0
    start = 0
    cur_sum = 0
    end = 0
    i = 0
    while i < len(arr):
        cur_sum += arr[i]
        if cur_sum < 0:
            start = i
            cur_sum = 0
        else:
            if cur_sum > max_sum:
                max_sum = cur_sum
                end = i
        i += 1
    
    range = [start+1, end]
    return range, max_sum
        

arr = [8, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
range, max_sum = max_sub_array(arr)
print(max_sum)
print(range)
print(arr[range[0]:range[1]+1])