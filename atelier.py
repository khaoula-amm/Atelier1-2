#Atelier 1
#Exercice1
def factorial(x): # on a utiliser cette fonction pour calculer la factorial du x
      if x == 1:
          return 1
      else:
         return (x * factorial(x-1))
n=int(input("saisir un nembre"))
s=0
for i in range(1,n+1): # on a utiliser la boucle for pour calculer la somme de 1 a n
  s=s+factorial(i)/i  # s c'est la somme des séries
print(s)
#Exercice2
def conver(x): # pour convertir le nombre décimal en nombre binaire on a deviser par 2 et afficher le reste
       if x>1:
         conver(x//2)
       print(x % 2,end=" ") # on a utiliser "end=" pour ne sauter pas la ligne
n=int(input(" saisir le nombre svp:"))
conver(n)
#exercice3
def sum(n):
    if n==0:
        return 0
    else:
       return(n+sum(n-1)) # on utilisant "sum(n-1)"pour ajouter le nombre precedent
n=int(input("saisir le nombre n :"))
print(sum(n))
#exercice4
def fibo(x): # pour imprimer la série Fibonacci 
  if x==0:
     return 0
  elif x==1:
     return 1  
  else:# on a utilisé "fibo(x-1)" et "fibo(x-2)"pour calculer la somme du precedent et avant precedent
     return fibo(x-1) + fibo(x-2) 
n=int(input("saisir le nombre "))
for i in range(n): # on utilisant la boucle for pour imprimer la série Fibonacci jusqu'a le nombre n
    print(fibo(i),end=' ')
#exercice5
def compter(N): 
    nbr=0
    while N!=0: #on devise le nombre sur 10 
      N = int(N/10)
      nbr+=1    # on a utilise "nbr+=1" pour incrimante nbr jusqu'a avoir 0
    return nbr
N =int(input("saisir le nombr"))
print(compter(N))
#Exercice6
def tribulle(L):
    permut=True # on declare "permut=True" pour enter dans la boucle while
    while permut == True:
     permut=False
     for i in range(0,(len(L)-1)):
         if L[i]>L[i+1]:
             t=L[i] 
             L[i]=L[i+1]
             L[i+1]=t
             permut=True #  on declare "permut=True" pour enter dans la boucle while pour la 2 eme fois 
     len(L)==len(L)-1 # on arretant toujour avant la dernier
L=[11, 45, 8, 11, 23, 45, 23, 45, 89]
print("le tab est nom tri",L)
tribulle(L)
print("le tab est  tri",L)
#Exercice7
def invrse(ch):
  inv=" "   # on a utilise "range(len(ch)-1,-1,-1)" pour avoir la boucle for du manier inversible
  for i in range(len(ch)-1,-1,-1)  :
   inv=inv+ch[i] 
  return inv  # inv pour afficher le mot du manier inversible
nom=str(input("entrer votre nom"))
print(invrse(nom))
     
#Exercice8
def freque(ch):
    fre =ch.count(n) # on utilisant "ch.count(n)"pour avoir le nombre du letre dans le mot
    return fre
ch =str(input("saisir ch:")) 
n =str(input("saisir n:"))   
print(freque(ch)) # pour appelle la fonction 

#Exercice9
def chercher(n,L):
    for i in range(len(L)): # on a utilise boucle dans boucle pour traiter la matrice
      for j in range(len(L[i])):
        if L[i][j]==n:
         return(i,j)# pour trouver la position du de n
L=[[1,7],[4,9]]
n=int(input("saisir le nombre"))
print(chercher(n,L))

#Atelier2
#Exercice1
def indi(L1,L2):
    L3=[]
    for i in range(0,len(L1)):
         if i%2!=0: 
           L3.append(L2[i]) #pour stocker dans la liste L3 les nombres impaire 
    for i in range(0,len(L2)):
           if i%2==0:
             L3.append(L2[i]) #pour stocker dans la liste L3 les nombres paire 
    return L3
L1=[3,6,9,12,15,18,21]
L2=[4,8,12,16,20,24,28]
print(indi(L1,L2)) #afficher la fonction indi 
#Exercice2
def morceau(L): 
   a=len(L)//3 # pour deviser la liste en 3 partie a est(1/3)
   b=len(L)*2//3 # b est 2/3 du liste
   L1=L[:a]
   L2=L[a:b]
   L3=L[b:]
   return L1[::-1],L2[::-1],L3[::-1] #inverse la liste on utilisant "L[::-1]"
L=[11, 45, 8, 23, 14, 12, 78, 45, 89]
print(morceau(L)) # affiche la liste apres devise est inverse chaque morceaux
#Exercice3
L1=[11, 45, 8, 11, 23, 45, 23, 45, 89]
s={} # cree une set vide pour stocker dans elle le resulta
for i in L1: # boucle for pour traiter tout la liste 
  if i in s: # on a utilise la boucle if pour que si i existe dans s on incrimante
       s[i]+=1
  else:
        s[i]=1
print(s)
#Exercice4
S1={23, 42, 65, 57, 78, 83, 29} 
S2={57, 83, 29, 67, 73, 43, 48}
inter={n for n in S2 if n in S1 } # on stocke dans "inter "si l'element existe dans S1 et dans S2
print(inter) #afficher inter
set1={n for n in S1 if n not in S2}# on stocke dans "set 1 "si l'element existe dans S1 et non dans S2
print(set1) #afficher set1
#Exercice5
L=[47, 64, 69, 37, 76, 83, 95, 97] 
D={'Yassine':47, 'Imane':69, 'Mohammed':76, 'Abir':97}
L1=[]
for i in L:
    if i in D.values():# on utilisant "D.values()" pour checher si l'element existe dans le dictionnaire 
        L1.append(i) # pour stocker dans la liste L1
print(L1) # afficher la liste L1

