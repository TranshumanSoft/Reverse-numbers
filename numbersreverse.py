number = int(input("Introduce a number, please: "))
numlist = [0]
counter = 0
while True:
    counter = counter + 1
    numlist.append(counter)
    if counter == number:
        break
numlist.reverse()
print(numlist)