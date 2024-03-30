
# 1a)
tall = 3 + 1
tall = tall * 2

# svaret er 8
print("Svaret er", tall)
print("Svaret er " + str(tall))
print(f'Svaret er {tall}')


# 1b)
tekst = "a" + "c"
tekst = tekst + "b"

# svaret er "acb"
print("Svaret er " + tekst)


# 1c)
j = 5
i = 10

while i<j:
    i = i + 2
    j = j - 1

# j er 5
print("Svaret er " + str(j))


# 1d
tallene = [1, 6, 4, 2]
a = 0
b = 0

for tall in tallene:
    if tall < 3:
        a = a + tall
    else:
        b = b + tall

# a * b = 30
print(a * b)


# 1e
def kalkuler(tall):
    if tall < 5:
        return tall*2
    else:
        return tall
    
a = kalkuler(4+3)

# Tallet er 7
print(a)


#1f
class Tall:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def m1(self, c):
        self._b = self._b + c
    
    def m2(self):
        self._a = self._a + self._b
    
    def m3(self):
        return 2*self._a
    
t = Tall (3,2)
t.m1(1)
t.m2()
t.m2()

# prints 22
print(4+t.m3())


#2a)
a = [5, 2, 4]
b = a[0]
b = b +1

# prints 5
print(a[0])


#2b)
a = [10, 8 ,7]
b = a
c = b
b[0] = 3
c[1] = 4

# [3, 4, 7]
print(a)


#2c)
class Person:
    def __init__(self, alder):
        self._alder = alder

    def doble_alder(self):
        self._alder = self._alder * 2

    def hent_alder(self):
        return self._alder
    
    def alder_som_maaneder(self):
        return self._alder * 12
    
p1 = Person(3)
p2 = p1
p3 = Person(5)
p4 = p3
p1.doble_alder()
print(p1.hent_alder())
print(p2.hent_alder())
print(p3.alder_som_maaneder())
print(p4.hent_alder())

# 6, 6, 60, 5
# p2 = p1 is an alias.


#3a)
def penger(femkroninger, kronestykker):
    return ((femkroninger * 5) + kronestykker)

assert penger(2,3) == 13


#3b)
def barnMedVoksen(alder1, alder2):
    return (alder1 >= 18 and alder2 < 18) or (alder2 >= 18 and alder1 < 18)   


assert barnMedVoksen(18, 5) == True
assert barnMedVoksen(10, 20) == True
assert barnMedVoksen(20, 30) == False
assert barnMedVoksen(5, 5) == False



#3c)
def allePositive(tallene):
    for tall in tallene:
        if(tall < 0):
            return False
        return True
    
#1)Den returnerer True dersom første tall er positiv, men det betyr ikke at alle tall i "tallene" er positive
    
#2)    
# listTall = [2,-1,-1]
# print(allePositive(listTall))

#3)
def allePositive(tallene):
    check = True
    for tall in tallene:
        if(tall < 0):
            check = False
    return check
    
listTall = [2,-1,-1]
assert allePositive(listTall) == False


#3d)
def fyllTilTi(tallene):
    if len(tallene) > 10:
        print("Listen inneholder mer enn 10 tall")
        list = []
        for i, tall in enumerate(tallene):
            print(tall)
            if i <= 10-1:
                list.append(tall)
        return list
    else:
        list = []
        for tall in tallene:
            list.append(tall)
        if len(list) < 10:
            for i in range(0, 10-len(list)):
                list.append(0)
        return list
                
liste = [1,2,3]
print(fyllTilTi(liste))


#3e)
# class Node:
#     def __init__(self, verdi):
#         self._verdi = verdi
#         self._neste = None

#     def settInn(self, ny):
#         self._neste = ny


# listeStart = Node("a")
# node_b = Node("b")
# listeStart.settInn(node_b)


#3f)
class Node:
    def __init__(self, verdi):
        self._verdi = verdi
        self._neste = None

    def settInn(self, ny):
        self._neste = ny

    def skrivMeg(self):
        print(self._verdi)
        if self._neste != None:
            neste = self._neste.skrivMeg()
      

listeStart = Node("a")
#listeStart.skrivMeg()
node_b = Node("b")
#node_b.skrivMeg()
listeStart.settInn(node_b)
#listeStart.skrivMeg()

ny = Node("c")
ny.settInn(listeStart)
listeStart = ny
listeStart.skrivMeg()

#4a)
