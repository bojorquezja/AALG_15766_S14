lab=[[1,1,1,1,1,1,1,1],
     [1,1,0,1,1,1,0,1],
     [1,1,1,1,0,1,1,1],
     [0,1,0,1,1,0,1,1],
     [1,1,0,1,1,1,1,1],
     [1,1,1,0,0,1,0,1],
     [1,0,1,1,1,0,1,1],
     [1,1,1,1,1,1,1,1]]

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
        
        
op=0
print(f"{caminos(lab, 0,0)} caminos con {op} operaciones")