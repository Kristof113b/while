import random

count = 0

for _ in range(20):
    szam = random.randint(1, 12)
    if szam % 3 == 0:
        print(szam)
        count += 1

print("3-mal osztható számok darabszáma:", count)
