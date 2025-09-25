import numpy as np


a  = np.array([2.5,6.5,]) 

## Array de 2 dimensoes

B = np.array([[1,2,3],[4,5,6]])
print(B)

# indexando o array
print(B[0,1])  # Acessa o elemento na primeira linha, segunda coluna
print(B[0,:])  # Acessa a primeira linha inteira
print(B[:,1])  # Acessa a segunda coluna inteira

# funcoes para criação de arrays
c= np.zeros((3))    # Cria um array 1x3  preenchido com zeros
print(c)
print(c.dtype)

D = np.zeros((2,3))  # Cria um array 2x3 preenchido com zeros
print(D)

E = np.ones((5))   # Cria um array 1x5 preenchido com uns
print(E)

f = np.arange(0,10)
print(f)    # Cria um array com valores de 0 a 9
#ou 

g = np.arange(10)   # Cria um array com valores de 0 a 9
print(g)

H=np.random.uniform(2,3)
print(H)

#operações aritméticas 

I = np.array([[1,2],[3,4]])
J = np.array([[6,7],[8,9]])
print(J)

print(I+J)   # Soma elemento a elemento
print(I*J)  # Multiplicação elemento a elemento
print(np.dot(I,J))  # Multiplicação de matrizes 

#solução de sistemas de equações lineares

A = np.array([[1,2],[3,4]])
B = np.array([9,8])
X = np.linalg.solve(A,B)
print(X)
