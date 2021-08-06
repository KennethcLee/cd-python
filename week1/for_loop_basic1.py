for j in range (151):
    print(j)

for j in range(5, 1001, 5):
    print(j)

for j in range(1, 101):
    if (j % 10 == 0):
        print('Coding Dojo')
    elif (j % 5 == 0):
        print('Coding')
    else:
        print(j)

for j in range(1, 101):
    if (j % 5 == 0):
        print('Coding ', end ="") 
        if (j % 2 == 0): 
            print('Dojo', end ="")
        print("") 
    else:
        print(j)

sum = 0
for j in range (500001):
    if (j % 2 != 0):
        sum += j
print(sum)

for j in range(2018, 0, -4):
    print(j)

def flexCounter(lowNum, highNum, mult):
    for j in range(lowNum, highNum + 1):
        if (j % mult == 0):
            print(j)

flexCounter(2, 19, 3)