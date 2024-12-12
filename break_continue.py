# break
for i in range(12):
    if(i == 9):
        break
    print("5 X", i+1, "=", 5 * (i + 1))


# continue
for i in range(12):
    if(i == 9):
        print('skip the itteration')
        continue
    print("5 X", i+1, "=", 5 * (i + 1))


i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


for i in range(1, 11):
    if i == 5:
        print("Number 5 encountered! Breaking out of the loop.")
        break
    print(f"Processing number: {i}")


for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(f"Odd number: {i}")


