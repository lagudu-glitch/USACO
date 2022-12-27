def main ():
    N = int (input())

    a = input ().split ()
    a = [int (i) for i in a]
    a.sort (reverse=True)

    b = input ().split ()
    b = [int (i) for i in b]

    comb = 1
    poss = []

    for i in a:
        buff = 0
        for j in b:
            if (i <= j):
                buff += 1
        poss.append(buff)

    for i in range(N):
        comb *= poss[i] - i
    print (comb)
if __name__ == "__main__":
    main ()
