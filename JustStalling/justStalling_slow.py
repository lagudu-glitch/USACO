def permutation (a, b, cntr):
    if len (a) == 0:
        return []

    if len(a) == 1:
        if (a[0] > b[cntr]):
            return []
        return [a]

    curr = []

    for i in range (len(a)):
        m = a[i]
        if (m > b[cntr]):
            continue
        remLst = a[:i] + a[i+1:]
        for p in permutation(remLst, b, cntr+1):
            curr.append([m] + p)
    return curr

def main ():
    N = int (input())

    a = input ().split ()
    a = [int (i) for i in a]

    b = input ().split ()
    b = [int (i) for i in b]

    poss = 0
    comb = permutation (a, b, 0)
    print (comb)
    for perm in comb:
        if (len(perm) == N):
            poss += 1
    print (len (comb))
    
if __name__ == "__main__":
    main ()
