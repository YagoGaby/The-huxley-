
vetor = []  
quant_p = int(input())


for i in range(quant_p):
    par_Modelo = input("".upper())
    par_Comparacao = input("".upper())
    for j in range(len(par_Modelo)):
        if par_Modelo[j]== 'A':
            vetor.append('T')
        if par_Modelo[j]== 'C':
            vetor.append('G') 
        if par_Modelo[j]== 'G':
            vetor.append('C')
        if par_Modelo[j]== 'T':
            vetor.append('A')
    branco="".join(vetor)
    if par_Comparacao == branco:
        print("COMPLEMENTARES")
    else:
        print("NAO COMPLEMENTARES")
        print(branco)
    branco=[]
    vetor=[]