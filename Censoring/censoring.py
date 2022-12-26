def censor (S, T):
    i = len (T) - 1
    ub = len (S)
    while (i < ub):
        if (S[i-len(T):i] == T):
            S = S[0:i-len(T)] + S[i::]
            ub = len (S)
            i = i - 3
        i += 1
    
    return (S)
    
def main ():
    f_r = open ("censor.in", "r")
    f_w = open ("censor.out", "w")
    S = f_r.readline ().split ()[0]
    T = f_r.readline ().split ()[0]

    S = censor (S, T)
    print ("{}".format (S), file=f_w)
    f_r.close ()
    f_w.close ()

if __name__ == "__main__":
    main ()