def maximizar_troca_de_figurinhas(figMaria, figJoao, A, B):

    controleMaria = 0
    controleJoao = 0 
    i = 0
    j = 0
    m = 0
    n = 0

    for i in range(int(A)):
      for j in range(int(B)):
        if figMaria[i] == figJoao[j]:
          controleMaria += 1
 
    for m in range(int(B)):
      for n in range(int(A)):
        if figJoao[m] == figMaria[n]:
          incontroleJoaodj += 1
   
    if (int(A) - int(controleMaria)) < (int(B) - int(controleJoao)):
        return print(f"O máximo de figurinhas para troca é:{int(A) - int(controleMaria)}")
    else:
        return print(f"O máximo de figurinhas para troca é:{int(B) - int(controleJoao)}")

if __name__ == '__main__':
    A, B = input().split(' ')
    figurinhas_da_maria = input().split(' ')
    figurinhas_da_joao = input().split(' ')
    maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao, A, B)