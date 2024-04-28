#1a) 8
#1b) print("b" + t1)
#1c) or
#1d) liste = [1, 1, 3]
#1e) 2
#1f) tall += 1
#1g) bok["a"].append(8) 


#3a)

def pris_inkl_frakt(varepris):
    if varepris >= 1000:
        return varepris
    elif varepris >= 500 and varepris < 1000:
        return varepris + 50
    else:
        return varepris + 80
    

assert pris_inkl_frakt(300) == 380
assert pris_inkl_frakt(600) == 650
assert pris_inkl_frakt(1300) == 1300

#3d)

def forkort_setning(kortOrd, setning):
    setningNy = ""
    for ord in setning.split():
        if not ord == kortOrd:
            setningNy = setningNy + ord + " "
    return setningNy

setning = "en krabbe skal en dag ut av skallet"
print(forkort_setning("skal", forkort_setning("en", setning)))

#4a)

class Emne:
    def __init__(self, emnekode, studenter, rettere):
        self._emnekode = emnekode #string
        self._studenter = studenter #dict with studen as objects
        self._rettere = rettere #list of rettere as objects

#4b)
    def _administrer(self):
        avslutt = False

        while not avslutt:
            print("Emnekode: " + str(self._emnekode))
            print("Velg en av følgende kommande: \n"
                  "O: Ny Oblig \n"
                  "F: Frist ute, start retting \n"
                  "L: Lag eksamensliste \n"
                  "A: Avslutt")
            tasteValg = input("Skriv inn din kommando: ")
            tasteValg = tasteValg.strip().upper()
            print(tasteValg)
            if tasteValg == "O":
                print(self._opprettOblig())
            elif tasteValg == "F":
                self._startRetting()
            elif tasteValg == "L":
                self._skrivEksamensListe()
            elif tasteValg == "A":
                avslutt = True
                print("Du har avlsuttet programmet. \n")
            else:
                print("Du har tastet inn ugyldig kommando, prøv på nytt. \n")
                
    def _opprettOblig(self):
        return NotImplemented
    
    def _startRetting(self):
        return NotImplemented
    
    def _skrivEksamensliste(self):
        return NotImplemented


#4c)
class Student:
    def __init(self, brukernavn, fullNavn):
        self._brukernavn = brukernavn
        self._fullNavn = fullNavn
        self.resultater = {}

    def registrer(self, obligId, resultat):
        self._resultater[obligId] = resultat

    def altGodkjent(self, antObliger):
        antGodkjent = 0
        for oblig, resultater in self._resultater.items():
            antGodkjent += resultater

        if antGodkjent == antObliger:
            return True
        else:
            return False
        
#4d)
class Retter:
    def __init__(self, brukernavn):
        self._brukernavn = brukernavn

    def _vurder(self, filnavn):
        return 1
    

#4e)
class Oblig:
    def __init__(self, obligId, frist, statusRetting):
        self._obligId = obligId
        self._frist = frist #ååmmdd
        self._statusRetting = False

    def _klarForRetting(self, dagensDato):
        if self._frist < dagensDato and self._statusRetting == False:
            return True
        else:
            return False
    
    def _hentBesvarelser(self):
        dict = {} # key = studentID, values = besvarelse fil navn
        filnavn = self._obligId + ".txt"
        with open(filnavn, 'r') as infile:
            for line in infile:
                lineData = line.strip().split()
                dict[lineData[0]] = lineData[1]
        return dict

#4f)
    def fordelRetting(self, besvarelserDict, rettereList):
        resultater = {} #key = studentID, value = results of vurder()
        antallRettere = len(rettereList)
        retterNr = 0
        for studentId, besvarelse in besvarelserDict.items():
            retter = rettereList[retterNr]
            resultat = retter.vurder(besvarelse)
            resultater[studentId] = resultat
            retterNr += 1
            if retterNr == antallRettere:
                retterNr = 0
        self._statusRetting = True
        return resultater

        









# studenter = {1111: "student"}
# rettere = ["retter1", "retter2"]
# emnekode = 12345

# testEmne = Emne(emnekode, studenter, rettere)
# testEmne._administrer()