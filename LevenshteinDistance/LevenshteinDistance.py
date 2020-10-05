# LevenshteinDistance is using dynamic programming
# Assuming the cost of chaning from str1(i chars) to str2(j chars) is f(i,j)
# three cases:
# 1. str1 -> str2 by adding the last char, cost of adding is Ca
#    str1 has i chars now, str2 has j chars, adding one more char to str1 to make it equal to str2
#    it's eqivalent to change from (i) chars to j-1 chars, whose cost is f(i, j-1), plus the cost of adding one more char at i+1 for str1
#    then str1 is i + new char ==> i+1, and str2 is j-1 + new char ==> j
#    total cost is f(i, j-1) + Ca, where Ca is always 1
# 2. str1 -> str2 by deleting the last char, cost of deleting is Cd
#    str1 has i chars now, str2 has j chars, deleting the last char of str1, 
#    actually is changing from (i-1)  chars to j chars, its cost is f(i-1, j)
#    total cost is f(i-1, j) + Cd, where Cd is always 1
# 3. str1 -> str2 by substituting the last char, cost of adding is Ct
#    str1 has i chars now, str2 has j chars, we substitude the last one, 
#    so it's changing from (i-1)  chars to (j-1) chars, cost is f(i-1, j-1)
#    total cost is f(i-1, j-1) + Ct, 
#    where Ct can be 1 or 0 (if two chars to be sutstituted are the same) 
# So f(i,j) = min(f(i-1,j-1)+1, f(i-1,j)+1, f(i-1,j-1) + 0/1)

def levenshtein_dist(str1, str2):
    f = [[x for x in range(len(str2)+1)] for y in range(len(str1)+1)]
    for i in range(1, len(str1)+1):
        f[i][0] = i # f[i-1][0]+1 

    print_f(f, len(str1), len(str2))

    print("-"*30)

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            cost_1 = f[i][j-1] + 1
            cost_2 = f[i-1][j] + 1 
            if str1[i-1] == str2[j-1]:
                ct = 0
            else:
                ct = 1
            cost_3 = f[i-1][j-1] + ct 
            f[i][j] = min(cost_1, cost_2, cost_3)
    print_f(f, len(str1), len(str2))
    return f[-1][-1]

def print_f(m, row, col):
    # m is a 2d matrix
    for i in range(row+1): 
        for j in range(col+1): 
            print(str(m[i][j]) + ",", end = "")
        print("\n")

s1 = "1test"
s2 = "mte1s3t"
steps = levenshtein_dist(s1, s2)
print(steps)