import LinearProbingHash

SIZE = 1000

def hash(key):
    return (key>>8)|((key&0xff)<<16)

def getNumsFromInputFile(n):
    nums=[]
    fin = open("in"+str(n)+".txt")
    numsString = fin.readline().split();
    for numString in numsString:
        nums.append(int(numString))
    return nums

def processNums(f,ft,nums,name):
    linearHash = LinearProbingHash.LinearProbingHash(SIZE)
    quadraticTable=[None] * SIZE
    doubleTable=[None] * SIZE
    collision=[0] * SIZE
    
    linearCT = 0
    linearC = 0
    quadraticCT = 0
    doubleCT = 0
    linearOut = ""
    quadraticOut = ""
    doubleOut = ""

    for num in nums:
        #linear
        linearC = 0

        index = num % SIZE
        while(linearHash.isTaken(hash(index))):
            print("index",hash(index),"is taken")
            linearC = linearC + 1
            linearCT = linearCT + 1
            index = (index + 1)%SIZE
        print("SET:",linearHash.set(hash(index),index*2))

        index = num % SIZE - 1
        count = 0
        #What is wrong here?
        while(linearHash.get(hash(index))!=(num*2)):
            #f.write("GET:"+str(index)+"="+str(linearHash.get(index))+"\n")
            linearC = linearC + 1
            linearCT = linearCT + 1
            count = count + 1
            index = (index + 1)%SIZE
            if(count > SIZE):
                break
        print("NEXT")
        #quadratic
        quadraticC = 0
        index = num % SIZE
        j=1
        count = 0
        while(quadraticTable[index]!=None):
            quadraticC = quadraticC + 1
            quadraticCT = quadraticCT + 1
            index = (index + j*j)%SIZE
            j=j+1
            if(count > 12):
                break
            count = count + 1
            print(count)
        quadraticTable[index]=num

        index = num % SIZE
        j=1
        count = 0
        while(quadraticTable[index]!=num):
            quadraticC = quadraticC + 1
            quadraticCT = quadraticCT + 1
            index = (index + j*j)%SIZE
            j=j+1
            if(count > 12):
                break
            count = count + 1
            print(count)
        #double
        doubleC = 0
        index = num % SIZE
        j=1
        count=0
        while(doubleTable[index]!=None):
            doubleC = doubleC + 1
            doubleCT = doubleCT + 1
            index = (index + j*j)%SIZE
            j=j+1
            if(count > 12):
                break
            count = count + 1
            print(count)
        doubleTable[index]=num

        index = num % SIZE
        j=1
        doubleFactor = 7
        while(doubleTable[index]!=num):
            doubleC = doubleC + 1
            doubleCT = doubleCT + 1
            index = (doubleFactor+index)%SIZE


        numStr = str(num)
        dbl = num*2
        dblStr = str(dbl)
        f.write(numStr+" : "+dblStr+" -> "+dblStr+", collisions " + str(linearC) + "\n")
        f.write(numStr+" : "+dblStr+" -> "+dblStr+", collisions " + str(quadraticC) + "\n")
        f.write(numStr+" : "+dblStr+" -> "+dblStr+", collisions " + str(doubleC) + "\n")
        f.write("\n")

    f.write("Linear    "+str(linearCT)+" collisions\n")
    f.write("Quadratic "+str(quadraticCT)+" collisions\n")
    f.write("Double    "+str(doubleCT)+" collisions\n")

    ft.write("\n")
    ft.write("*** Linear probing "+name+" Order Start ***\n")
    ft.write("\n")
    ft.write("print table.size()=SIZE\n")
    for index in range(0,10):
        key = linearHash.get(index)
        if(key != None):
            ft.write("index="+str(index)+" key="+str(key)+" value="+str(key*2)+"\n")
    ft.write("\n")
    ft.write("Linear probing "+str(linearCT)+" collisions\n")
    ft.write("\n")
    ft.write("*** Linear probing "+name+" Order End ***\n")
    ft.write("\n")
    ft.write("\n")

    ft.write("*** Quadratic probing "+name+" Order Start ***\n")
    ft.write("\n")
    ft.write("print table.size()=SIZE\n")
    for index in range(0,10):
        key = quadraticTable[index]
        if(key != None):
            ft.write("index="+str(index)+" key="+str(key)+" value="+str(key*2)+"\n")
    ft.write("\n")
    ft.write("Quadratic probing "+str(quadraticCT)+" collisions\n")
    ft.write("\n")
    ft.write("*** Quadratic probing "+name+" Order End ***\n")
    ft.write("\n")
    ft.write("\n")

    ft.write("*** Double Hashing probing "+name+" Order Start ***\n")
    ft.write("\n")
    ft.write("print table_.size()=SIZE\n")
    for index in range(0,10):
        key = doubleTable[index]
        if(key != None):
            ft.write("index="+str(index)+" key="+str(key)+" value="+str(key*2)+"\n")
    ft.write("\n")
    ft.write("Double Hashing probing "+str(doubleCT)+" collisions\n")
    ft.write("\n")
    ft.write("*** Double probing "+name+" Order End ***\n")
    ft.write("\n")

def process(n):
    f = open("out"+str(n)+"_collisions_actual.txt","w")
    ft = open("out"+str(n)+"_tables_actual.txt","w")
    f.write("Format of output\n")
    f.write("key:  value  ->  retrievedValue , collisions number Collisions\n")
    f.write("Linear total number Collisions\n")
    f.write("Quadratic total number Collisions\n")
    f.write("Double hashing total number Collisions\n")
    f.write("\n")
    f.write("*** Random Order Start ***\n")
    f.write("\n")

    nums=getNumsFromInputFile(n)
    processNums(f,ft,nums,"Random")
    f.write("\n")
    f.write("\n")
    nums.sort()
    processNums(f,ft,nums,"Ascending")
    f.write("\n")
    f.write("*** Ascending Order End ***\n")
    f.write("\n")
    f.write("Format of output\n")
    f.write("key:  value  ->  retrievedValue , collisions number Collisions\n")
    f.write("Linear total number Collisions\n")
    f.write("Quadratic total number Collisions\n")
    f.write("Double hashing total number Collisions\n")
    f.write("\n")
    f.write("*** Descending Order Start ***\n")
    f.write("\n")
    nums.sort(reverse=True)
    processNums(f,ft,nums,"Descending")
    f.write("\n")
    f.write("*** Descending Order End ***\n")
    f.write("\n")

    f.close()
    ft.close()


for i in [150,160,170,180]:
    process(i)

print("Done.")
lph = LinearProbingHash.LinearProbingHash(1)