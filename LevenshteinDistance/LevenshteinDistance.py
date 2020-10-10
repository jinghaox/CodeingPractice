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
#        "" m a r c h 
#      "" 0 1 2 3 4 5      # "" -> m, need Insert(1),     "" ->ma, need Insert(2)
#      c  1 1 2 3 3 4      # ""c-> m, need substitude(1), ""c->ma, need substitude(1) + insertion(1), ""c->marc == ""->mar, 3 steps
#      a  2 2 1 2 3        # ""ca->marc, 
#      r  3
#      t  4
#        first column, ""->m, need insert(1); ""->ma, need insert(2)

def levenshtein_dist(str1, str2):

    f = [[x for x in range(len(str2)+1)] for y in range(len(str1)+1)]
    for i in range(1, len(str1)+1):
        f[i][0] = i # f[i-1][0]+1 

    print_f(f, len(str1), len(str2))

    print("-"*30)

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            # if the last chars are the same, can skip it, since no operation is needed
            if str1[i-1] == str2[j-1]:
                f[i][j] = f[i-1][j-1]
            else:
                # in this case, since last chars are not the same, so Ct is always 1
                cost_1 = f[i][j-1] + 1
                cost_2 = f[i-1][j] + 1 
                cost_3 = f[i-1][j-1] + 1 
                f[i][j] = min(cost_1, cost_2, cost_3)
    print_f(f, len(str1), len(str2))
    return f[-1][-1]


def levenshtein_dist_optimize(str1, str2):
    """
    Example: when i goes to 3

      j   0 1 2 3 4
    i    '' C A R T 
    0  '' 0 1 2 3 4      <--- evenEdits
    1  M  1 1 2 3 4      <--- oddEdits
    2  A  2 2 1 2 3      <--- evenEdits
    3  R  3 1 2 3 4      <--- currEdits (actually is the oddEdits of i = 1), then update currentEdits[0] to 3, then update currentEdit[1:4] one by one
                                         so initial value is [3,1,2,3,4], after update it's [3,3,2,1,2]
    4  C
    5  H
    """
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2
    evenEdits = [x for x in range(len(small) + 1)]
    oddEdits = [None for x in range(len(small) + 1)]
    for i in range(1, len(big) + 1):
        if i % 2 == 1:
            currentEdits = oddEdits
            previousEdits = evenEdits
        else:
            currentEdits = evenEdits
            previousEdits = oddEdits
        currentEdits[0] = i
        for j in range(1, len(small) + 1):
            if big[i - 1] == small[j - 1]:
                currentEdits[j] = previousEdits[j - 1]
            else:
                currentEdits[j] = 1 + min(previousEdits[j - 1], previousEdits[j], currentEdits[j - 1])
    return evenEdits[-1] if len(big) % 2 == 0 else oddEdits[-1]

def levenshtein_dist_final(str1, str2):
    # the above even, odd thing is tricky, actually what we need is two rows, and use a temp to swap those two rows
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2
    prevEdits = [x for x in range(len(small) + 1)]
    currEdits = [None for x in range(len(small) + 1)]
    for i in range(1, len(big)+1):
        currEdits[0] = i
        for j in range(1, len(small)+1):
            if big[i-1] == small[j-1]:
                currEdits[j] = prevEdits[j-1]
            else:
                currEdits[j] = 1 + min(prevEdits[j - 1], prevEdits[j], currEdits[j-1])
        temp = currEdits
        currEdits = prevEdits
        prevEdits = temp
    
    return prevEdits[-1]


def print_f(m, row, col):
    # m is a 2d matrix
    for i in range(row+1): 
        for j in range(col+1): 
            print(str(m[i][j]) + ",", end = "")
        print("\n")

s1 = "cart"
s2 = "march"
steps = levenshtein_dist_final(s1, s2)
print(steps)