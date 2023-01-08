# Time complexity of this function is O (n^3)

def unique ():
    
    inp = open ("whereami_bronze_dec19/10.in", "r")
    out = open ("out/10.out", "w")

    size = int (inp.readline().strip())
    seq = inp.readline().strip()

    k = 1

    while (k != size):
        prev = k

        for i in range(0, size - (k - 1)):
            for j in range (0, size - (k - 1)):
                if (i == j):
                    continue

                if (seq[i: i + k] == seq[j: j + k]):
                    k = k + 1
                    break

            if (prev != k):
                break
        
        if (prev == k):
            break
    
    print (k, file=out)

if __name__ == "__main__":
    unique ()