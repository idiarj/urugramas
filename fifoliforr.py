import time

def ingresarDatos():
    nombresAct = []
    Ti = []
    t = []
    nAct = int(input("Ingrese el numero de actividades: "))
    for l in range(nAct):
        nName = input(f"Ingresa el nombre de la actividad {l + 1}:")
        nTi = int(input(f"Ingresa el tiempo de inicio de esta actividad: "))
        nt = int(input(f"Ingresa el tiempo que dura la activdad: "))
        nombresAct.append(nName)
        Ti.append(nTi)
        t.append(nt)
    q = int(input("Ingrese el cuantum para el Round Robin: "))
    return nombresAct, Ti, t, q

#nombres, Ti, t, quantum = ingresarDatos()

def fifo(ActNames, initialTime, time):
    print("\t\t\t\t\t\t\t\t\t\t\t\tEsto es FIFO\n")
    clock = ['clock']
    numberAct = len(ActNames)
    names = ActNames[:]
    Ti = initialTime[:]
    t = time[:]
    calcTi = Ti[:]
    Tf = [None] * numberAct
    T = [None] * numberAct
    E = [None] * numberAct
    I = [None] * numberAct
    c = min(Ti)
    clock.append(c)
    x = 0
    sumT, sumE, sumI = 0, 0, 0
    while x < numberAct:
        for i in range(numberAct):
            if calcTi[i] != None and c >= calcTi[i]:
                Tf[i] = c + t[i]
                c = Tf[i]
                clock.append(c)
                calcTi[i] = None
                T[i] = Tf[i] - Ti[i]
                sumT += T[i]
                E[i] = T[i] - t[i]
                sumE += E[i]
                I[i] = t[i]/(Tf[i] - Ti[i])
                sumI += I[i]
                break
        x+=1

    LC = len(clock) - 1

    names.insert(0, 'Nombres')
    Ti.insert(0, 'Ti')
    t.insert(0, 't')
    Tf.insert(0, 'Tf')
    T.insert(0, 'T')
    E.insert(0, 'E')
    I.insert(0, 'I')

    clckF = clock[len(clock) - 1] + min(Ti[1:])

    names.insert(LC, '')
    Ti.insert(LC, '')
    t.insert(LC , '')
    Tf.insert(LC, '')
    T.insert(LC , '')
    E.insert(LC , '')
    I.insert(LC , '')

    avgT = sumT/numberAct
    avgE = sumE/numberAct
    avgI = sumI/numberAct

    matriz = [clock, names, Ti, t, Tf, T, E, I]

    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            print("{: <15}".format(str(matriz[j][i])), end='')
        print()

    print(f"{clckF} <- Clock Final")
    print(f"El promedio del tiempo de retorno es {round(avgT, 3)}\n")
    print(f"El promedio del tiempo de espera es {round(avgE, 3)}\n")
    print(f"El promedio de eficiencia es {round(avgI, 4)}")

    return clckF, avgI

def lifo(ActNames, initialTime, time):
    print("\t\t\t\t\t\t\t\t\t\t\t\tEsto es LIFO\n")
    clock = ['clock']
    numberAct = len(ActNames)
    names = ActNames[:]
    Ti = initialTime[:]
    # print(Ti)
    t = time[:]
    calcTi = Ti[:]
    calct = t[:]
    calcTi.reverse()
    calct.reverse()
    Tf = [None] * numberAct
    T = [None] * numberAct
    E = [None] * numberAct
    I = [None] * numberAct
    c = min(Ti)
    clock.append(c)
    x = 0
    sumT, sumE, sumI = 0, 0, 0
    while x < numberAct:
        for i in range(numberAct):
            if calcTi[i] != None and c >= calcTi[i]:
                Tf[i] = c + calct[i]
                c = Tf[i]
                clock.append(c)
                calcTi[i] = None
                break
        x+=1

    Tf.reverse()
    for j in range(numberAct):
        T[j] = Tf[j] - Ti[j]
        sumT += T[j]
        E[j] = T[j] - t[j]
        sumE += E[j]
        I[j] = t[j] / (Tf[j] - Ti[j])
        sumI += I[j]

    LC = len(clock) - 1

    names.insert(0, 'Nombres')
    Ti.insert(0, 'Ti')
    t.insert(0, 't')
    Tf.insert(0, 'Tf')
    T.insert(0, 'T')
    E.insert(0, 'E')
    I.insert(0, 'I')

    clckF = clock[len(clock) - 1] + min(Ti[1:])

    names.insert(LC, '')
    Ti.insert(LC, '')
    t.insert(LC , '')
    Tf.insert(LC, '')
    T.insert(LC , '')
    E.insert(LC , '')
    I.insert(LC , '')

    avgT = sumT/numberAct
    avgE = sumE/numberAct
    avgI = sumI/numberAct

    matriz = [clock, names, Ti, t, Tf, T, E, I]

    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            print("{: <15}".format(str(matriz[j][i])), end='')
        print()

    print(f"{clckF} <- Clock Final")
    print(f"\nEl promedio del tiempo de retorno es {round(avgT, 3)}")
    print(f"El promedio del tiempo de espera es {round(avgE, 3)}")
    print(f"El promedio de eficiencia es {round(avgI, 4)}")

    return clckF, avgI

def RoundRobin(ActNames, initialTime, time, q):
    print("\t\t\t\t\t\t\t\t\t\t\t\tEsto es Round Robin\n")
    clock = ['clock']
    numberAct = len(ActNames)
    names = ActNames[:]
    Ti = initialTime
    t = time
    calct = t[:]
    Tf = [None] * numberAct
    T = [None] * numberAct
    E = [None] * numberAct
    I = [None] * numberAct
    c = min(Ti)
    clock.append(c)

    sumT, sumE, sumI = 0, 0, 0
    while sum(calct) > 0:
        for i in range(numberAct):
            if calct[i] > 0:
                if calct[i] <= q:
                    c += calct[i]
                    clock.append(c)
                    Tf[i] = c
                    calct[i] = 0
                else:
                    c += q
                    clock.append(c)
                    calct[i] -= q

    for j in range(numberAct):
        T[j] = Tf[j] - Ti[j]
        E[j] = T[j] - t[j]
        I[j] = t[j] / T[j]
        sumT += T[j]
        sumE += E[j]
        sumI += I[j]

    LC = len(clock) - 1

    names.insert(0, 'Nombres')
    Ti.insert(0, 'Ti')
    t.insert(0, 't')
    Tf.insert(0, 'Tf')
    T.insert(0, 'T')
    E.insert(0, 'E')
    I.insert(0, 'I')

    clckF = clock[len(clock) - 1] + min(Ti[1:])

    avgT = sumT / numberAct
    avgE = sumE / numberAct
    avgI = sumI / numberAct

    matriz = [names, Ti, t, Tf, T, E, I]

    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            print("{: <15}".format(str(matriz[j][i])), end='')
        print()

    print()
    print(f"{clckF} <- Clock Final Round Robin")
    print(f"\nEl promedio del tiempo de retorno es {round(avgT, 3)}")
    print(f"El promedio del tiempo de espera es {round(avgE, 3)}")
    print(f"El promedio de eficiencia es {round(avgI, 4)}")

    return clckF, avgI

# nombres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a1', 'b1', 'c1', 'd1', 'e1', 'f1' ,'g1', 'h1', 'I1', 'j1', 'k1', 'l1', 'm1']
# Ti = [ 2, 9, 8, 7, 6, 5, 40, 4, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 3, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]
# t = [17, 47, 14, 32, 48, 23, 13, 37, 24, 4, 25, 34, 26, 38, 15, 31, 42, 21, 45, 23, 36, 22, 49, 18, 39, 27, 46, 16, 30, 44, 35, 20, 50, 19, 33, 41, 28, 40, 29]
# quantum = 4

nombres, Ti, t, quantum = ingresarDatos()

iniFIFO = time.time()
clckFIFO, IFIFO = fifo(nombres, Ti, t)
finFIFO = time.time()
TTFIFO = finFIFO - iniFIFO

print()

iniLIFO = time.time()
clckLIFO, ILIFO = lifo(nombres, Ti, t)
finLIFO = time.time()
TTLIFO = finLIFO - iniLIFO

print()

iniRR = time.time()
clckRR, IRR = RoundRobin(nombres, Ti, t, quantum)
finRR = time.time()
TTRR = finRR - iniRR



print(f"\nEL tiempo que tardo en realizarse FIFO fue {round(TTFIFO, 5)} segundos, el tiempo que tardo en realizarse "
      f"con LIFO {round(TTLIFO, 5)} segundos y el tiempo que tardo en realizarse con Round Robin {round(TTRR, 5)} segundos")

print(f"\nClock con FIFO {clckFIFO}, Clock con LIFO {clckLIFO}, Clock con RR {clckRR}")

if clckFIFO== clckLIFO == clckRR:
    print("Felicidades! El clock dio igual, lo que significa que el programa esta bien!")
    print("Bueno, felicidades a mi realmente, yo se mucho, profe pongame 20")
else:
    print("bobolon")

if IFIFO > ILIFO and IFIFO > IRR:
    print(f"La eficiencia con FIFO ({IFIFO}) fue mayor a la de LIFO ({ILIFO}) y RR ({IRR})")
elif ILIFO > IFIFO and ILIFO > IRR:
    print(f"La eficiencia con LIFO ({ILIFO}) fue mayor a la de FIFO ({IFIFO}) y RR ({IRR})")
elif IRR > ILIFO and IRR > IFIFO:
    print(f"La eficiencia con RR ({IRR}) es mayor a la de FIFO ({IFIFO}) y LIFO ({ILIFO})")