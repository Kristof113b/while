szam = int(input("Adj meg egy páros számot: "))

while szam % 2 != 0:
    szam = int(input("Ez nem páros! Adj meg egy páros számot: "))

print("Köszönöm! A megadott páros szám:", szam)
