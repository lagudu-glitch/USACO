def read ():
    N = []
    E = []

    num = int (input ())
    for i in range (num):
        pos = input ().split ()
        if (pos[0] == 'E'):
            E.append ([int (pos[1]), int (pos[2]), i])
        else:
            N.append ([int (pos[1]), int (pos[2]), i])
    
    return N, E

def collision (N, E):
    plots = [float ('inf')] * (len (N) + len (E))

    for cowN in N:
        for cowE in E:
            g_cowE = cowN[0] - cowE[0] 
            g_cowN = cowE[1] - cowN[1]

            if ((g_cowE < 0) or (g_cowN < 0)):
                continue

            if (g_cowE > g_cowN):
                if ((g_cowE < plots[cowE[2]]) and g_cowN < plots[cowN[2]]):
                    plots[cowE[2]] = g_cowE

            elif (g_cowN > g_cowE):
                if ((g_cowN < plots[cowN[2]]) and g_cowE < plots[cowE[2]]):
                    plots[cowN[2]] = g_cowN
            
    return plots

def sort (mat):
    for i in range (1, len (mat)):
        key = mat[i]
        j = i - 1
        while (j >= 0 and key[1] < mat[j][1]):
            mat[j+1] = mat[j]
            j -= 1
        mat[j + 1] = key
    
    return mat

def main ():
    f = open ("test.out", "w")

    (N, E) = read ()
    E = sort (E)
    plots = collision (N, E)
    # E = [[3,5],[4,6],[10,4]]
    # print (E)
    for plot in plots:
        if (plot == float ('inf')):
            print ("Infinity", file=f)
        else:
            print ("{}".format(plot), file=f)

if __name__ == "__main__":
    main ()

