import time

def stop_watch(func):
    # note: decorator will be called multiple times in recursive call 
    def wrappe(*args, **kwargs):
        start_time = time.time()
        ret = func(*args, **kwargs)
        print("time: {}".format(time.time()-start_time))
        return ret
    return wrappe

def max_subset(s):
    # recursion version, takes long time, and has limitations on the max recursion depth
    # first find max of s
    # ..............x max x --------------
    # then for ....x max_l x......... (s[0:i-1]), find its max again like for s
    # then for ----x max_r x------ (s[i+2:n+1]), find its max again like for s
    # the max sum is max + max_l + max_r + ...

    print(s)
    if s == []:
        return 0
    if len(s) == 1:
        return s[0]
    sum = 0
    max_v = max(s)
    ix = s.index(max_v)

    n = len(s)
    sum += max_v + max_subset(s[ix+2:n+1]) + max_subset(s[0:ix-1])
    return sum

@stop_watch
def maxSubsetSumNoAdjacent(array):
    """
    Time: O(n)
    Space: O(1)
    maxSum[i] = max (maxSum[i-1], maxSum[i-2] + arr[i])
    [7, 10, 12, 7, 9, 14]
     7, 10, 19, 
     when we go to the 2nd 7
     the max sum must be either 19 (just before current 7), 
     or the previous maxsum (10) + current 7 = 17, no other choices
    """
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    second = array[0]
    first = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
    return first

s = [7, 10, 12, 7, 9, 14]
ret = max_subset(s)

s = list(range(10000))
ret = maxSubsetSumNoAdjacent(s)
print(ret)