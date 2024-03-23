
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
    