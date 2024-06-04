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
    
#4b)
class Kategori:

    def __init__(self, kategorinavn, rettListe):
        self._kategorinavn = kategorinavn
        self._rettListe = rettListe

    def hentOkRetter(self, allergiListe):    
        nyRettListe = []
        for rett in self._rettListe:
            if rett.sjekkInnholdOK(allergiListe):
                nyRettListe.append(rett)
        
        return nyRettListe

#4c)
class Meny:

    def __init__(self, kNavneListe):
        self._kNavneListe = kNavneListe
        self._meny = self.byggMeny() 

    def byggMeny(self):
        meny = {}
        for kategoriNavn in self._kNavneListe:
            kategoriFilNavn = str(kategoriNavn + str(".txt"))
            print(kategoriFilNavn)
            meny[kategoriNavn] = self._lesKategoriFil(kategoriFilNavn)

        return meny

    def hentRedusertMeny(self, allergiListe):
        redusertMeny = {}
        for kategoriNavn, kategori in self._meny.items():
            nyKategori = Kategori(kategoriNavn, kategori.hentOkRetter(allergiListe))
            redusertMeny[kategoriNavn] = nyKategori
        return redusertMeny
    
    def _lesKategoriFil(self, kNavn):
        retter = []
        with open(kNavn, "r") as katfil:
            for linje in katfil:
                linje = linje.split()
                retter.append(Rett(linje[0], linje[1], linje[2:]))
        nyKat = Kategori(kNavn, retter)
        return nyKat
    
#4d)
class Kunde:

    def __init__(self, tlfNummer, allergier):
        self._tlfNummer = tlfNummer
        self._allergier = allergier

    def velgRetter(self, meny):
        menyValg = []
        redusertMeny = meny.hentRedusertMeny(self._allergier)
        for kategoriNavn, kategori in redusertMeny.items():
            print(f'{kategoriNavn} har følgende retter: ')
            for rett in kategori._rettListe:
                print(rett)

            valg = input("Tast in navnet på retten for å velge, eller tom-linje for å hoppe til neste kategori: ")
            print(valg)
            if valg != "":
                menyValg.append(str(valg))
        
        print("Da har vi gått gjennom hele menyen")
        return menyValg
            
#4e)
class Takeaway:

    def __init__(self, kNavnListe, kundeFilNavn):
        self.meny = Meny(kNavnListe)
        self.kundeDict = self._lesKundefil(kundeFilNavn)
    
    def betjenKunde(self, tlfNummer):
        bestilling = self.kundeDict[tlfNummer].velgRetter(self.meny)
        self._lagOgLeverMat(bestilling)

    def _lagOgLeverMat(self, bestilling):
        print("Kundends bestilling er: ")
        for rett in bestilling:
            print(rett)

    def _lesKundefil(self, kundefilnavn):
        kunder = {}
        with open(kundefilnavn, "r") as kundefil:
            for linje in kundefil:
                data = linje.strip().split()
                kunder[data[0]] = Kunde(data[0], data[1:])
                
        return kunder

def Hovedprogram():
    kategorier = ["Forretter", "Hovedretter", "Desserter"]
    takeawayBestilling = Takeaway(kategorier, "kunder.txt")
    kundeId = input("oppgi et telefonnummer: ")
    while kundeId != "":
        takeawayBestilling.betjenKunde(kundeId)
        kundeId = input("Oppgi telefonnr: ")

#Hovedprogram()

#5)

def check_nested(lst):
    for val in lst:
        if isinstance(val, list):
            return True
        return False
    
def godkjenn(aldre):

    if check_nested(aldre) == False:
        for val in aldre:
            if val >= 18:
                return True
        return False
    else:
        count = []
        for valList in aldre:
            check = False
            for valNested in valList:
                if valNested >= 18:
                    check = True
            if check:
                count.append(1)
        
        if len(aldre) == sum(count):
            return True
        else:
            return False

def godkjenn2(aldre):

    for val in aldre:
        voksen = False
        for val2 in val:
            if val2 >= 18:
                voksen = True
        if voksen == False:
            return False
    return True


test = [10, 2, 18]

print(godkjenn2(test))
