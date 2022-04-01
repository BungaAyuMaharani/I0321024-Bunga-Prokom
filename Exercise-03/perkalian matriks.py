print("====================")
matriksA= [[2,2,2]
           [3,3,3]
           [4,4,4]]
matriksB= [[1,2,3]
           [4,5,6]
           [7,8,9]]
#membuat matriks yang menampung hasil perkalian
matriksC=[]

print("mulai mengali dua matriks :")

for x in range (0, len(matriksA)):
    print()
#membuat skalar (matrik satu baris) untuk menampung hasil perkalian
    baris =[]
    for y in range (0, len(matriksA[0])) :
        total=0; 
        for z in range (0, len(matriksA)):
            total = total + (matriksA[x] [z] * matriksB[z] [y])
        baris.append(total)
    matriksC.append(baris)

print("====================")

#cetak hasil
for x in range (0, len(matriksC)) :
    for y in range (0, len(matriksC[0])):
        print ("matriksC [x] [y]", end '    ') 
    print()

