import pdb

pdb.set_trace()
def maximo(l):
    max = -1000000000
    for i in l:
        if i>max:
            max = i
    return max

listas = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]

maximos = [maximo(l) for l in listas]
print(maximos)


def primo(n):
	es_primo = True
	lista_primos = []
	for i in range(2, n):
		if n%i == 0:
			es_primo = False
	if(es_primo):
		return n

lista = [3, 4, 8, 5, 5, 22, 13]
primos = list(filter(primo, lista))
print(primos)
