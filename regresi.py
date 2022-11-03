import csv,os,time
os.system('cls')

#inisialisasi
bulan = []
x = []
y = []
xy = []
xpangkat2 = []
ypangkat2 = []
nomor = []

baris = int(input('Banyak Baris: '))
n = baris

#list nomor
for i in range(baris):
    nomor.append(i+1)

#list Bulan
print('\nNama-nama bulan :')
for i in range(baris):
    dataBulan = str(input('- '))
    bulan.append(dataBulan)

#list durasi (x)
print('\nData x :')
for i in range(baris):
    datax = int(input('- '))
    x.append(datax)

#list y
print('\nData y :')
for i in range(baris):
    datay = int(input('- '))
    y.append(datay)

#list xy
for i in range(baris):
    xy.append(x[i]*y[i])

#list x^2
for i in x:
    xpangkat2.append(i**2)

#list y^2
for i in y:
    ypangkat2.append(i**2)


#total (baris baru)
nomor.append(' ')
bulan.append('Total')
x.append(sum(x))
y.append(sum(y))
xy.append(sum(xy))
xpangkat2.append(sum(xpangkat2))
ypangkat2.append(sum(ypangkat2))

#mencari nilali b
b = (n*xy[baris]-x[baris]*y[baris])/(n*xpangkat2[baris]-x[baris]**2)

#mencari nilai a
