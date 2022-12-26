def possible (sick, milk_ty, misc):
    milk_pos =[]
    for person in sick:
        for milk in milk_ty:
            if (person[0] != milk[0]):
                continue

            if (milk[2] >= person[1]):
                continue

            if (person[0] == milk[0]):
                misc[milk[1] - 1] += 1
            
    for i in range (0, len (misc)):
        if (misc[i] >= len (sick)):
            milk_pos.append (i + 1)
    
    return milk_pos

def min_dose (milk_pos, milk_ty, misc):
    dose = 0

    for milk in milk_pos:
        for person in milk_ty:
            if (misc[person[0] - 1] == 1):
                continue

            if (person[1] == milk):
                dose += 1
                misc[person[0] - 1] = 1
    
    return dose

def main ():
    f = open ("badmilk.in", "r")

    vals = f.readline().split()

    misc_milk = [0] * int (vals [1])
    misc_person = [0] * int (vals [0])


    milk_ty = []
    for i in range (0, int (vals[2])):
        buff = f.readline().split()
        buff = [int (i) for i in buff]
        milk_ty.append (buff)

    sick = []
    for j in range (0, int (vals [3])):
        buff = f.readline().split()
        buff = [int (i) for i in buff]
        sick.append (buff)
    

    milk_pos = possible (sick, milk_ty, misc_milk)
    dose = min_dose (milk_pos, milk_ty, misc_person)

    f_w = open ("badmilk.out", "w")
    print ("{}".format (dose), file=f_w)

    f.close ()
    f_w.close ()

if __name__ == "__main__":
    main ()
       
