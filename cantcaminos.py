lab=[[1,1,1,1,1,1,1,1],
     [1,1,0,1,1,1,0,1],
     [1,1,1,1,0,1,1,1],
     [0,1,0,1,1,0,1,1],
     [1,1,0,1,1,1,1,1],
     [1,1,1,0,0,1,0,1],
     [1,0,1,1,1,0,1,1],
     [1,1,1,1,1,1,1,1]]

mem=[[-1]*len(lab[0]) for _ in range(len(lab))]

def imprime(mat):
    for f in mat:
        for c in f:
            print(f"{c},",end="")
        print()
    print()

def caminosR(lab, f,c):
    global op
    op += 1
    if f == len(lab)-1 and c == len(lab[0])-1 :
        if lab[f][c] == 1:
            return 1
        else:
            return 0
    elif c == len(lab[0])-1:
        if lab[f][c] == 1:
            return caminosR(lab, f+1,c)
        else:
            return 0
    elif f == len(lab)-1:
        if lab[f][c] == 1:
            return caminosR(lab, f,c+1)
        else:
            return 0
    else:
        if lab[f][c] == 1:
            return caminosR(lab, f,c+1)+caminosR(lab, f+1,c)
        else:
            return 0

def caminosPD(lab, mem, f,c):
    global op
    op += 1
    if mem[f][c] != -1:
        return mem[f][c]
    elif f == len(lab)-1 and c == len(lab[0])-1 :
        if lab[f][c] == 1:
            mem[f][c] = 1
            return mem[f][c]
        else:
            return 0
    elif c == len(lab[0])-1:
        if lab[f][c] == 1:
            mem[f][c] = caminosPD(lab, mem, f+1,c)
            return mem[f][c]
        else:
            return 0
    elif f == len(lab)-1:
        if lab[f][c] == 1:
            mem[f][c] = caminosPD(lab, mem, f,c+1)
            return mem[f][c]
        else:
            return 0
    else:
        if lab[f][c] == 1:
            mem[f][c] = caminosPD(lab, mem, f,c+1)+caminosPD(lab, mem, f+1,c)
            return mem[f][c]
        else:
            return 0
        
        
op=0
print(f"{caminosR(lab, 0,0)} caminos con {op} operaciones")
op=0
print(f"{caminosPD(lab, mem, 0,0)} caminos con {op} operaciones")

