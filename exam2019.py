print("---------------------------------- 1 ----------------------------------------")

#1a)
print(3)

#1b)
print("ad")

#1c)
print(17)

#1d)
print(9)

#1e)
print(16)

#1f)
print(32)


print("---------------------------------- 2 ----------------------------------------")

#2a)
print(49)

#2b)
print(60)

#2c)
print(49)

#2d)
print(49)

print("---------------------------------- 3 ----------------------------------------")

#3a
def vinnerlag(hjemmelag, bortelag, hjemmemaal, bortemaal):
    if hjemmemaal > bortemaal:
        return hjemmelag
    elif bortemaal > hjemmemaal:
        return bortelag
    elif hjemmemaal == bortemaal:
        return "uavgjort"

assert vinnerlag("Brann", "Molde", 2, 3) == "Molde"
assert vinnerlag("Brann", "Molde", 2, 2) == "uavgjort"
assert vinnerlag("Brann", "Molde", 3, 2) == "Brann"

#3b
def forkort_lagliste(lagliste):
    kortListe = []

    for lag in lagliste:
        if lag not in kortListe:
            kortListe.append(lag)

    return kortListe

liste = ["Brann", "Molde", "Brann"]
assert forkort_lagliste(liste) == ["Brann", "Molde"]

#3c)
def legg_inn_null_maal(lagliste):
    dict = {}

    for lag in lagliste:
        dict[lag] = 0

    return dict

assert legg_inn_null_maal(["Brann", "Molde"]) == {"Brann": 0, "Molde": 0}

#3d)
def ekstraher_lagliste(fn):
    
    lagListe = []
    with open(fn, "r") as infile:
        for line in infile:
            dataLine = line.strip().split()
            lagListe.append(dataLine[0])
            lagListe.append(dataLine[1])
    
    return(forkort_lagliste(lagListe))

print(ekstraher_lagliste("file.txt"))

#3e)
def regn_poengsum(fn):

    lagListe = ekstraher_lagliste(fn)
    lagOrdbok = legg_inn_null_maal(lagListe)

    with open(fn, "r") as infile:
        for line in infile:
            lineData = line.strip().split()
            resultat = vinnerlag(lineData[0], lineData[1], lineData[2], lineData[3])
            if resultat == lineData[0] or resultat == lineData[1]:
                lagOrdbok[resultat] += 1

    return lagOrdbok

print(regn_poengsum("file.txt"))

#3f)
def gull(lagoversikt):
    
    vinnerlag = ""
    hPoengsum = 0

    for lag in lagoversikt:
        if lagoversikt[lag] > hPoengsum:
            hPoengsum = lagoversikt[lag]
            vinnerlag = lag

    return vinnerlag

#3g)
def finn_gull(fn):
    print(gull(regn_poengsum(fn)))

finn_gull("file.txt")


print("---------------------------------- 4 ----------------------------------------")

#4a)
class Rett:

    def __init__(self, navn, pris, innholdListe):
        self._navn = navn
        self._pris = pris
        self._innholdListe = innholdListe

    def sjekkInnholdOK(self, allergiListe):
        for allergi in allergiListe:
            if allergi in self._innholdListe:
                return False
            
        return True
    
    def __str__(self):
        innhold = ", ".join(self._innholdListe)
        msg = ("Retten " + self._navn + ", kostner " + str(self._pris) + " per rett og inneholder: " + innhold + ".")
        return msg