def longest_palindromic_substr(string):
    """ Non-DP 
        Time: O(n^2)
        Space: O(1)

               i
        odd: abcba, where str[i] is in the center, so we start from s[i-1:i+1], 
        then check s[i-2:i+2], ... s[i-x:i+x] until to the edge, return [i-x+1, i+x], the length is 2x-1

                i
        even: abba, where str[i] is not in the center, but str[i-1]==str[i], so we start from s[i-1:i],
        then check s[i-2:i+1], s[i-x-1:i+x], return [i-x, i+x], the length is 2x
    """
    currentLongest = [0, 1]
    for i in range(1, len(string)):
        odd = getLongestPalindromeFrom(string, i - 1, i + 1)
        even = getLongestPalindromeFrom(string, i - 1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        # here the max's key is calculating the length of a two element list x[0, 1], i.e. x[1] - x[0]
        currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
    return string[currentLongest[0] : currentLongest[1]]

def getLongestPalindromeFrom(string, leftIdx, rightIdx):
    # helper function
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    return [leftIdx + 1, rightIdx]


def LongestPalindromicSubstring(s):
    """ DP algorithm
        time complexity: O(n^2)
        space complexity: O(n^2)
        dp[i][j]: if 1, means str[i:j] is palindrome
        dp[i][j] can be derived from dp[i+1][j-1] if s[i]==s[j]
        so we don't need to re-cal dp[i][j] from the scratch
        for each j (from 0 to n)
        check dp[i][j], where i=0,1,2,...j
        so we still need to check str[0:j], str[1:j], str[2:j] until str[j-1:j]
    """
    if s=="":
        return s
    max_len = 1000
    dp = [[0 for x in range(max_len)] for y in range(max_len)]
    max_p = 0

    len_s = len(s)
    for j in range(len_s):
        # for i, we only need to check up to j
        for i in range(0, j):
            # dp[i][j] will be 0 or 1 
            # for a given i&j, if previous dp[i+1][j-1] is true, and s[i]==s[j], then dp[i][j] is true

            dp[i][j] = (((j-i<=2) or dp[i+1][j-1]) and s[i] == s[j])

            # when dp[i][j] is true, then we check if its length is the longest
            if (dp[i][j]):
                # j-i+1 is the length of the palindrome substring
                if (j-i+1 > max_p):
                    max_p = j-i+1;
                    res = s[i:j+1]
    # print2d(dp, len_s)
    return res

def print2d(array, n):
    for i in range(n):
        for j in range(n):
            print("{},".format(array[i][j]), end="")
        print("\n")

# this dp algorithm looks like is constructing a 2D array 
# i.e. if s[i] == s[j], set dp[i][j]=>1
# but actually not
# see the screenshot attached as an example
# code below demos the return is bcbzb, but should be bcb

def my_longest_palin_2d_array(s):
    # note: this won't return the correct longest palindrome substring
    if s=="":
        return s
    max_len = 1000
    dp = [[0 for x in range(max_len)] for y in range(max_len)]
    max_p = 0

    len_s = len(s)
    for j in range(len_s):
        for i in range(0, j):
            if s[i] == s[j]:
                dp[i][j] = 1

            if dp[i][j] == 1:
                if (j-i+1 > max_p):
                    max_p = j-i+1;
                    res = s[i:j+1]
    return res

s = "bcbzb"
# ret = LongestPalindromicSubstring(s)
ret = longest_palindromic_substr(s)
print(ret)

