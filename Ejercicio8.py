nums = []

min = int(input("Defina el menor numero: "))
max = int(input("Defina el numero maximo: "))

for i in range (min, max):
    nums.append(i)

imp = []
for j in nums:
    if j % 2 == 1:
        imp.append(j)

print(imp)
