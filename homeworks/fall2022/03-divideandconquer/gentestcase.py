import random
numpoints = int(input("How many points? "))
with open(str(numpoints)+".txt", "w") as f:
    # numpoints = 
    print(numpoints, file = f)
    for i in range(numpoints):
        x = random.uniform(-50000,50000)
        y = random.uniform(-50000,50000)

        print(x,y,file=f)
    print(0,file=f)
