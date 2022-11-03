'''
Program untuk menemukan regresi Linier berganda
( Statistika )
-------------------------------------------------

created by Muhammad Yusuf
Prodi Informatika
Institut Teknologi Indonesia
'''


import csv, time, os
os.system('cls')


#inisialisasi
responden=[]
x1=[]
x2=[]
y=[]
x1pangkat2=[]
x2pangkkat2=[]
ypangkat2=[]
x1kaliy=[]
x2kaliy=[]
x1kalix2=[]



baris =  int(input('Masukkan jumlah baris: '))

for i in range(baris):
    responden.append(i+1)



#input data x1
print('\nMasukkan data x1: ')
for i in range(baris):
    datax1= int(input())
    x1.append(datax1)



#input data x2
print('\nMasukkan data x2:')
for i in range(baris):
    datax2=int(input())
    x2.append(datax2)


#input data x
print('\nMasukkan data y:')
for i in range(baris):
    datay=int(input())
    y.append(datay)


#data x1^2
for i in x1:
    x1pangkat2.append(i**2)


#data x2^2
for i in x2:
    x2pangkkat2.append(i**2)


#data y^2
for i in y:
    ypangkat2.append(i**2)



#data x1 * y
for i in range(baris):
    x1kaliy.append(x1[i]*y[i])


#data x2*y
for i in range(baris):
    x2kaliy.append(x2[i]*y[i])


#data x1*x2
for i in range(baris):
    x1kalix2.append(x1[i]*x2[i])



#baris total
responden.append('Total')
x1.append(sum(x1))
x2.append(sum(x2))
y.append(sum(y))
x1pangkat2.append(sum(x1pangkat2))
x2pangkkat2.append(sum(x2pangkkat2))
ypangkat2.append(sum(ypangkat2))
x1kaliy.append(sum(x1kaliy))
x2kaliy.append(sum(x2kaliy))
x1kalix2.append(sum(x1kalix2))

    
total_x1 = x1[baris]
total_x2 = x2[baris]
total_y = y[baris]
total_x1pangkat2 = x1pangkat2[baris]
total_x2pangkkat2 = x2pangkkat2[baris]
total_ypangkat2 = ypangkat2[baris]
total_x1kaliy = x1kaliy[baris]
total_x2kaliy = x2kaliy[baris]
total_x1kalix2 = x1kalix2[baris]

sigma1 = total_x1pangkat2-(total_x1**2/baris)
sigma2 = total_x2pangkkat2-(total_x2**2/baris)
sigma3 = total_ypangkat2-(total_y**2/baris)
sigma4 = total_x1kaliy-(total_x1*total_y/baris)
sigma5 = total_x2kaliy-(total_x2*total_y/baris)
sigma6 = total_x1kalix2-(total_x1*total_x2/baris)


b1 = (sigma2*sigma4-sigma6*sigma5)/(sigma1*sigma2-sigma6**2)
b2 = (sigma1*sigma5-sigma6*sigma4)/(sigma1*sigma2-sigma6**2)
a = total_y/baris-b1*(total_x1/baris)-b2*(total_x2/baris)

print(f'''
b1 = {b1}
b2 = {b2}
a = {a}
y = a + b1x1 + b2x2 = {a} + {b1}x1 + {b2}x2
''')


while True:
    ask = str(input('Apakah anda ingin menyimpannya? (y/n)  > ')).lower()
    time.sleep(0.2)
    print('Mohon tunggu....')
    time.sleep(1.3)
    if ask == 'y':
        name = str(input('Masukkan nama file: '))+'.csv'
        f = open(name,'w')
        w = csv.writer(f)
        w.writerow(['Responden','X1','X2','Y','X1^2','X2^2','Y^2','X1.Y','X2.Y','X1.X2'])
        f.close()

        #cetak
        f2=open(name,'a')
        w = csv.writer(f2)

        for i in range(baris+1):
            cetak=[responden[i],x1[i],x2[i],y[i],x1pangkat2[i],x2pangkkat2[i],ypangkat2[i],x1kaliy[i],x2kaliy[i],x1kalix2[i]]
            w.writerow(cetak)

        w.writerow([''])
        w.writerow(['N =',baris])
        w.writerow(['b1 =',b1])
        w.writerow(['b2 =',b2])
        w.writerow(['a =',a])
        w.writerow(['y =','a + b1x1 + b2x1 =', f'{a} + {b1}x1 + {b2}x2'])
        f2.close()
        print('Menyimpan....')
        time.sleep(2)
        print('Berhasil Menyimpan...')
        break

    elif ask == 'n':
        print('Terimakasih.. Program Selesai..')
        break

    else:
        print('Pilihan tidak tersedia..')
