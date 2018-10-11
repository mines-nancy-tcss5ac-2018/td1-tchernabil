#Euleur : problème 16
def digits (n):
    #conversion du nombre en liste
    #méthode 1
    N=list(str(n))
    Somme=0
    for i in range (len(N)):
        Somme+=int(N[i])
    return Somme

def digits2 (n):
    #méthode 2
    L=[]
    while n>0:
        L.append(n%10)
        n=n//10
    Triée=[]
    for k in range (len(L)):
        Triée.append(L[len(L)-1-k])
    Somme=0
    for i in range (len(Triée)):
            Somme+=int(Triée[i])    
    return Somme

assert digits(123) == 6
assert digits2(123) == 6

print (digits(2**1000))

#Euler : problème 22

f=open('p022_names.txt', 'r')
L=[]
for e in f:
    L.append(e)
A=L[0].split(',')
Triée=sorted(A)

def conversionalphabet (lettre):
    alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range (len(alpha)):
        if lettre==alpha[i]:
            return i+1
    return 0

assert conversionalphabet('E')==5

    
def namevalue(name):
    somme=0
    for i in range(len(name)):
        somme+=conversionalphabet(name[i])
    return somme

assert namevalue('COLIN')==53

def position(name,text):
    position=1
    for i in range(len(text)):
        if text[i]==name:
            return position
        position+=1
    return 'le nom ne figure pas dans le texte'

assert position ('"COLIN"',Triée)==938

def totalnamescore(text):
    score=0
    for i in range (len(text)):
        score+=namevalue(text[i])*position(text[i],text)
    return score

print(totalnamescore(Triée))
    
#Euleur : problème 55 (lychrel numbers)

def decompochiffres(n):
    #C'est la méthode de "digits2(n)"
    L=[]
    while n>0:
        L.append(n%10)
        n=n//10
    Triée=[]
    for k in range (len(L)):
        Triée.append(L[len(L)-1-k])
    return Triée

assert decompochiffres(123)==[1,2,3]

def recomponombre(liste):
    nombre=0
    for k in range(len(liste)):
        nombre+=(liste[len(liste)-1-k])*(10**(k))
    return nombre

assert recomponombre([1,2,3])==123

def palindrome(n):
    L=decompochiffres(n)
    compteur=0
    for k in range (len(L)//2):
        if L[k]==L[len(L)-1-k]:
            compteur+=1
    return compteur==(len(L)//2)

assert palindrome(134431)==True

def reverseadd(nombre):
    Decompo=decompochiffres(nombre)
    Decomporeverse=[]
    for k in range(len(Decompo)):
        Decomporeverse.append(Decompo[len(Decompo)-1-k])
    reverse=recomponombre(Decomporeverse)
    return nombre+reverse

assert reverseadd(47)==121

def lychrel(n):
    limite=0
    a=reverseadd(n)
    while palindrome(a)==False and limite<=50 :
        a=reverseadd(a)
        limite+=1
    return not palindrome(a)

assert lychrel(196)==True

def solve(n):
    compteur=0
    for k in range(n+1):
        if lychrel(k):
            compteur+=1
    return compteur

assert solve(196)==1

print(solve(10000))

