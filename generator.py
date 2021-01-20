import numpy as np

i: int = 10  #ilosc procesow do wygenerowania

p = []
at = []
bt = []
for a in range(0, i):
    p.append(a)
    bt.append(int(np.random.normal(loc=5,scale=2, size=1)))
    #at.append(int(np.random.randint(i)))
    correct = False
    while not correct:
        tempAt = np.random.randint(i)
        if tempAt not in at:
            at.append(tempAt)
            correct = True
        else:
            correct = False

with open('test.csv', 'w') as f:    #zapisanie danych do pliku
    f.write("%s,%s,%s\n" % ('pNumber', "burstTime", "arrivalTime"))
    for i in range (0, i):
        f.write("%s,%s,%s\n"%(p[i],bt[i],at[i]))