'''
Created on 11 de jan de 2017

@author: Racicley
'''

def manipula_inst():
    arq = open('db/binpack1.txt','r').readlines()
    count = 0
    lista_it = []

    for linha in arq[2:]:
        if(linha == " u120_01 \n"):
            break

        lista_it.append(int(linha.rstrip()))
        count = count + 1


    return lista_it

def gera_lrestrito(lista,alpha):
    lista_restrit = []
    for elemento in lista:
        if(min(lista) <= elemento and elemento <= min(lista) + alpha * (max(lista) - min(lista))):
            lista_restrit.append(elemento)
        else:
            continue
    return lista_restrit

def constroi(lista_itens, alpha):
    
    while(lista_itens):        
        i = 0
        
        lista_restrito = gera_lrestrito(lista_itens, alpha)
        
        if(len(mochilas.keys()) == 0):
            mochilas[0] = []
            mochilas[0].append(lista_restrito[i])
            
            lista_itens.remove(lista_itens[i])
            lista_restrito.remove(lista_restrito[0])
        else:
            for chave in range(len(mochilas.keys())):
                if(sum(mochilas[chave]) + lista_itens[i] <= capacidade):
                    
                    mochilas[chave].append(lista_restrito[i])
                    lista_itens.remove(lista_itens[i])
                    lista_restrito.remove(lista_restrito[0])
                    break
                elif(mochilas.__contains__(chave+1)):
                    continue
                else:
                    mochilas[chave + 1] = []
                    mochilas[chave + 1].append(lista_restrito[i])
                    
                    lista_itens.remove(lista_itens[i])
                    lista_restrito.remove(lista_restrito[0])   

if __name__ == '__main__':
    
    lista_restrito = []
    
    
    capacidade = 150
    #alpha = 0.81
    count = 0
    
    mochilas = {}
    
    #lista de itens a serem alocados nas mochilas
    lista_itens = manipula_inst()
    
    