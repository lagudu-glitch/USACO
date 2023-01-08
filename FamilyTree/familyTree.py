
def read ():
    f = open ('family.in', 'r')
    lines = f.readlines ()

    relation_lst = []
    for line in lines:
        relation_lst.append (line.split ())
    
    return relation_lst [1::], relation_lst [0:1]


def mother (cow, des, ans):
    for i in range (0, len(des)):
        if (cow == des[i]):
            return ans[i]
    return None

def is_ans (cow1, cow2, des, ans):
    gen = 0

    while (cow1 != None):
        if (cow1 == cow2):
            return gen

        cow1 = mother (cow1, des, ans)
        gen +=1
    
    return None

def main ():
    (relation_lst, cows) = read ()
    f = open ("family.out", "w")

    des = [row[0] for row in relation_lst]
    ans = [row[1] for row in relation_lst]

    non_dir = 0
    cow = cows[1]
    while (cow != None):
        if (is_ans (cow, cows[2], des, ans) != None):
            break
        cow = mother (cow, des, ans)
        non_dir += 1
    
    if (cow == None):
        print ("NOT RELATED", file=f)
        return
    
    gen = is_ans (cows[1], cows[2])

    if (gen == 1 and non_dir == 1):
        print ("SIBLINGS", file=f)



if __name__ == "__main__":
    main ()

    

