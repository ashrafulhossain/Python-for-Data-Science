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



total = 0
counter = 1

while True:
    total += counter
    print(f"Added {counter}, Total: {total}")
    if total > 20:
        print("Total exceeded 20, breaking out of the loop.")
        break
    counter += 1


num = 0

while num < 10:
    num += 1
    if num % 3 == 0:
        continue
    print(f"Current number: {num}")


for x in range(1, 5):
    for y in range(1, 5):
        print(f"Checking pair: ({x}, {y})")
        if x * y == 6:
            print("Pair found! Breaking out of the inner loop.")
            break



for x in range(1, 5):
    for y in range(1, 5):
        if x == 3 or y == 3:
            continue
        print(f"Processing pair: ({x}, {y})")

