monoOrDi = str(input("Are you doing a monohybrid or dyhibrid cross? "))

if monoOrDi.lower() == "monohybrid":
    monohybrid = True
else:
    monohybrid = False
    
def punnitSquareSim(geno1,geno2):
    results = [""]*4
    realcounter = 0
    for i in range(0,2):
        for j in range(0,2):
            #Selection to ensure that capital letter goes first
            if ord(geno1[i]) <= ord(geno2[j]):
                results[realcounter] = geno1[i] + geno2[j]
            else:
                results[realcounter] = geno2[j] + geno1[i]
                
            realcounter += 1
    return results
    
def punnitSquareDisplay(geno1,geno2,results):
    print("+----------+----------+----------+")
    print("|          |    "+geno2[0]+"     |    "+geno2[1]+"     |")
    print("+----------+----------+----------+")
    print("|    "+geno1[0]+"     |    "+results[0]+"    |    "+results[1]+"    |")
    print("|    "+geno1[1]+"     |    "+results[2]+"    |    "+results[3]+"    |")
    print("+----------+----------+----------+")


def genotypicRatio(results):
    stringCounterDict={}
    for i in range(0,4):
        if results[i] in stringCounterDict:
            stringCounterDict[results[i]] = stringCounterDict[results[i]] + 1
        else:
            stringCounterDict[results[i]] = 1
            
    if len(stringCounterDict) == 1:
        print("1:1")
    else:
        tempString = ':'.join(str(value) for value in stringCounterDict.values())
        print(tempString)
        
def probabilityCalculation(results):
    stringCounterDict={}
    for i in range(0,4):
        if results[i] in stringCounterDict:
            stringCounterDict[results[i]] = stringCounterDict[results[i]] + 25
        else:
            stringCounterDict[results[i]] = 25
    
    if len(stringCounterDict) == 1:
        print("100%")
    else:
        tempString = '% '.join(str(value) for value in stringCounterDict.values())
        print(tempString + "%")
        
    
finished = False

if monohybrid:
    geno1 = str(input("Enter first parents Genotype: "))
    geno2 = str(input("Enter second parents Genotype: "))
    results = punnitSquareSim(geno1,geno2)
    while (finished == False):
        print("Selection of results:")
        print("Press 1 to have punnit square displayed")
        print("Press 2 to have genotypic ratio displayed")
        print("Press 3 to display probabilities")
        print("Press 4 to exit")
        selection = int(input("Make Selection: "))
        if (selection == 1):
            punnitSquareDisplay(geno1,geno2,results)
        elif (selection == 2):
            #genotypic ratio
            genotypicRatio(results)
        elif (selection == 3):
            #calc probabilities
            probabilityCalculation(results)
        else:
            finished = True
            print("Thank you for using!")
else:
    geno11 = str(input("Enter first parents first Genotype: "))
    geno12 = str(input("Enter second parents firstGenotype: "))
    geno21 = str(input("Enter first parents second Genotype: "))
    geno22 = str(input("Enter second parents second Genotype: "))
    results1 = punnitSquareSim(geno11,geno12)
    results2 = punnitSquareSim(geno21,geno22)
    while (finished == False):
        print("Selection of results:")
        print("Press 1 to have punnit square displayed")
        print("Press 2 to have genotypic ratio displayed")
        print("Press 3 to display probabilities")
        print("Press 4 to exit")
        selection = int(input("Make Selection: "))
        if (selection == 1):
            punnitSquareDisplay(geno11,geno12,results1)
            punnitSquareDisplay(geno21,geno22,results2)
        elif (selection == 2):
            #genotypic ratio
            genotypicRatio(results1)
            genotypicRatio(results2)
        elif (selection == 3):
            #calc probabilities
            probabilityCalculation(results1)
            probabilityCalculation(results2)
        else:
            finished = True
            print("Thank you for using!")