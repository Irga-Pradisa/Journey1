# Belajar Python

print('TYPE DATA')
def belajar():
    print(str('Belajar Python'))
    print(int(8+10))
    print(str('Irga Ganteng'))
    print(float(10.4+11.6))
    print(bool(1))
    Name = input('Masukkan Nama Anda: ')
    Umur = input('Berapa Umur Anda :' )
    print(Name, Umur)
    Favorit_Song = [
        input('Masukkan Lagu Favorit Anda: '),
        input('Pencipta Lagu Favorit Anda: '),
        input('Band Kesukaan Anda: '),
    ]
    print(10>=10)
    print(10/50)
    print(100.9//11.8)
    name = 10+15
    name = 'Irga'
    print(name)
    x=y=z= '10.1, 60, Ganteng'
    print(x)
    
belajar()



print('LEARN BUILT-IN')
print('======================================')
print('Selamat Datang di  Indomaret')
print('======================================')
Nama_Barang = input('Masukkan Nama Barang Anda: ')
Harga_Barang = int(input('Masukkan Harga Barang Anda: '))
Jumlah_Barang = int(input('Masukkan Jumlah Barang Anda: '))
Diskon = int(input('Masukkan Diskon Anda: '))
Potongan_Harga = int((Harga_Barang * Jumlah_Barang) * Diskon / 100)
print('======================================')
print('Nama Barang Anda: ', Nama_Barang)
print('Harga Barang Anda: ', Harga_Barang)
print('Jumlah Barang Anda: ', Jumlah_Barang)
print('Diskon Anda: ', Potongan_Harga)
print('======================================')
print('Total Harga Anda: ', (Harga_Barang * Jumlah_Barang) - Diskon - Potongan_Harga)
print('======================================')
print('Terima Kasih Telah Berbelanja di Indomaret')



print('LEARN VARIABLES')

print('Jika x adalah 3, Berapa hasil x -=1?')
user_answer = float(input('Masukkan jawaban Anda: '))

if abs(user_answer - 2) < 0.001: 
    print('Your answer is correct!')
else:
    print('Your answer is INCORRECT!')
    print(f'Jawaban yang benar adalah: {2}')

print('Jika x adalah 3, Berapa hasil x *=321?')
user_answer = float(input('Masukkan jawaban Anda: '))
if abs(user_answer - 963) < 0.001: 
    print('Your answer is correct!')
else:
    print('Your answer is INCORRECT!')
    print(f'Jawaban yang benar adalah: {963}')



print('LEARN OPERATORS')

z = 10
i = 20

print(z == i)
print(z != i)
print(z > i)
print(z < i)
print(z >= i)
print(z <= i) 

print('======================================')
while True:
    user_answer = input('Masukkan Username Anda: ')
    if user_answer == 'irga' and len(user_answer) >= 8:
        print('Username Anda Benar')
        break
    else:
        print('Username Anda Salah')
        print('Silahkan Masukkan Username Anda yang Benar')
        continue
print('======================================')
while True:
    user_answer = input('Masukkan Email Anda: ')
    if user_answer == 'abogobogoba@gmail.com' and len(user_answer) >= 8:
        print('Email Anda Benar')
        break
    else:
        print('Email Anda Salah')
        print('Silahkan Masukkan Email Anda yang Benar')
        continue
print('======================================')
while True:
    user_answer = input('Masukkan Password Anda: ')
    if user_answer == 'ure_handsome' and len(user_answer) >= 8:
        print('Password Anda Benar')
        break
    else:
        print('Password Anda Salah')
        print('Silahkan Masukkan Password Anda yang Benar')
        continue

print('Login Berhasil')
print('======================================')



print('LEARN STRINGS')
print('======================================')
x = 'prdspractice' 
y = 'prdsadvance'

print('Index ke-5 dari x adalah: ', x[5])
print('Index ke-3 dari x adalah: ', y[3])
print('================================')
print('Jumlah karakter dari x adalah: ', len(x))
print('Jumlah karakter dari y adalah: ', len(y))
print('================================')
name1 = 'irga'
name2 = 'ure'
name3 = 'so handsome'
print('Nama saya adalah: ', name1 + ' ' + name2 + ' ' + name3)
print('================================')
print(f'{name1}\n{name2}\n{name3}')
print('================================')
print('''
'irga'
'ure'
'so_handsome'
''')

x = 'prds practice'
print(x.upper())
print(x.lower())
print(x.title())
print(x.capitalize())
print(x.replace('s', 'U', 1))
print(x.count('p'))

x = 'prds' 
y = 'practice'
z = 'advance'
print(x + ' ' + y + ' ' + z)

print('layout' + '3')
print('layout' * 3)

x = 'asep'
y = '3'
print(f'Hello my name is {x} and im yo {y}')

discount = 1000
cost = 10000
text_1 = f'Cost is {discount * 2}'
print(text_1)
text_2 = f'Cost is {cost * 2} and discount is {discount}'
print(text_2)

print('my name is \'izat\'')



print('================================')
print('LEARN LISTS') #Can be change use # () or [] or {}

x = ['asep', 12, 10.8, 'young'] #element utama
print(x)

#put in elemen
print(x[0])
print(x[-1])
print(x[1:3])

#in and not in
x = [ 8, 10, 12]                #element utama
print( 9 in x)
print( 20 not in x)

#re-assign elemen
x[1] = (1)
x[2] = (2)
print(x)

#plus element
x.append(20)#plus element
print(x)
x.extend([30, 40])#plus element
print(x)
x.insert(2, 50)
print(x)
x.remove(50)
print(x)

#BackSpace Element
x.pop(2) #bs by index
print(x)
x.clear() #all bs            #x.remove(20)   for remove by value
print(x)

#sort
x = [10, 20, 30, 40, 50]            #Element utama
x.sort()#sort by less to large
print(x)
x.sort(reverse=True)#sort by large to less bcs (reverse)
print(x)

x = ['asep', 'wkwkwkkw', 'ganteng']         #elemen utama
x.sort(key = len)#sort by words, from less to long
print(x)

z = x #if u want z follow x (not use copy)
print(z)   
z.reverse() #if u want reverse the list and variables x dont follow variable z (use copy) 
print(z)



print('================================')
print('LEARN TUPLES') ##Can not be change use ()

x = ('nia', 'asep', 'komang','nia', 'asep') #element utama
print(x)
print(x[1]) #if u want put by index
print(type(x))

total = x.count('asep') #if u want count of element
print(f'Maka total nama asep adalah {total}')
print(f'Maka index dari nia adalah {x.index("nia")}') #if u want find the index of element



print('================================')
print('LEARN SET') #Can be change but random use {}

x = {'nia', 'asep', 'komang','nia'}   #element utama
x.add('uo') #if u want add element
print(x)
x.remove('nia') #if u want remove element
print(x)
z = {'po', 'iu'}
x.update(z) #if u want add element from variable
print(x)

x.discard('ii') #if u want remove element (cannot be error if the elemnt not in the set)
print(x)
x.remove('uo') #if u want remove element 
print(x)

x = ('aiu', 'uua') # The element
y = ('uua', 'papa') # The element
uwu = set(x) | set(y)
print(uwu) #if u want add variable and variable

print(set(x).intersection(set(y))) #if u want find the same element
print(set(x).difference(set(y))) #if u want find the different element
u = set(x) ^ set(y)  #if u want find the different element all variable
print(u)



print('================================')
print('LEARN DICTIONARY') #for store data (key, value)

def Data() : #for store data
    Personal_Data = [
        'Name: asep',
        'Age: 20',
        "Hobby: Coding",
        "Favorite_Song: [What Makes You Beautiful, One Direction, Perfect, Ed Sheeran]",
    ]
    for data in Personal_Data :
        print(data)
Data()

print('================================')   
student = {  #for store data, and know keys, values, and items
    'name': 'asep',
    '20': 'Twenty years old',
    'Hobby': 'Coding',
}

name = student['name']
age = student['20']

print(name)
print(age)
all_keys = student.keys()
all_values = student.values()
all_items = student.items()
print(f'keys: {all_keys}')
print(f'values: {all_values}')
print(f'items: {all_items}')

print('================================')
student = {  #for correct in store data
    'asep': 'Asep',
    '20': 'Twenty years old',
    'Hobby': 'Coding',
}

print('asep')

student['asep'] = 'bubung'
student['Address'] = 'Jl. Raya No. 1' #if u want add element, the element not in the dictionary
student.update({'20': 'Twenty years'})
print(student)

print('================================')
student = {  #for remove in store data
    'asep': 'Asep',
    '20': 'Twenty years old',
    'Hobby': 'Coding',
}
student.pop('asep') #if u want remove element
print(student)
student.popitem() #if u want remove the last element
print(student)
student.clear() #if u want remove all element
print(student)
'''

'''
print('================================')

print('COLLECTION MULTIDIMENSION') #for sv data in listnlist,tuplentuple,setnset,dictndict

x = [ #for sv and store data in listnlist
    [50, 20, 10],
    [10, 30, 20],
    [15, 40, 30],
    'adep', # also can use string
    3.45, #also can use float or int
]
print(x[0][2]) #if u want put by index
print(x[3]) #if u want put by index
print(x[4]) #if u want put by index

print('================================')
x = ( #for sv and store data in tuplentuple
    (50, 20, 10),
    (10, 30, 20),
    (15, 40, 30),
    'pupu', # also can use string
    989, #also can use float or int
)
print(x[2][1]) #if u want put by index
print(x[3]) #if u want put by index
print(x[4]) #if u want put by index



print('================================')

print('FUNCTION BUILTIN TYPE DATA COLLECTION') #for store data in fnction sum,min,len 

x = [10, 20, 30, 40, 50]  #also can use string, float
print('Sum of x:', sum(x)) #if u want sum the element
print('Min of x:', min(x)) #if u want find the min element
print('Max of x:', max(x)) #if u want find the max element
print('Length of x:', len(x)) #if u want find the length of element



print('================================')

print('UNPACKING') #for unpacking data in list, tuple, set, dict
x = [1, 2, 3, 4, 5] #for unpacking data in list
y, z, u, *f = x #if u want unpacking data in list (*f for the rest of the list so it will be 4, 5)
print(y) #if u want put by index
print(z) #if u want put by index
print(*f) # *f is the rest of the list so it will be 4, 5 (the keyword * is used to unpack the list)

print('================================')   
x = {'name':'asep', 'age':18} #for unpacking data in dictionary
y, z = x.items() #if u want unpacking data in dictionary
print(y) #if u want put by index
print(z) #if u want put by index
y, z = x.values() #if u want unpacking data in dictionary
print(y) #if u want put by index
print(z) #if u want put by index

print('================================')
x = (1, 2, 3, 4, 5) #for combination packing nd unpacking data in tuple
y, z, *u, = x #if u want unpacking data in tuple
print(y) #if u want put by index
print(z) #if u want put by index
print(*u) # *f is the rest of the tuple so it will be 4, 5 (the keyword * is used to unpack the tuple)



print('================================')
print('CONDITIONAL STATEMENT') #for conditional statement in if, elif, else
Nama_Siswa = input('Masukkan Nama Anda: ')
Nilai_Siswa = int(input('Masukkan Nilai Anda: '))
if Nilai_Siswa >= 90:
    print('Nilai Anda A')
    print(f'Nama Anda {Nama_Siswa} dan Anda Lulus')
elif Nilai_Siswa >= 75:
    print('Nilai Anda B')
    print(f'Nama Anda {Nama_Siswa} dan Anda Lulus')
elif Nilai_Siswa >= 60:
    print('Nilai Anda C')
    print(f'Nama Anda {Nama_Siswa} dan Anda Lulus')
else:
    print('Nilai Anda D, GOBLOK KOE BELAJAR ATO GA')
    print(f'Nama Anda {Nama_Siswa} dan Anda Tidak Lulus')

print('================================')
x = int(input('Masukkan Angka: ')) #Chaining if, elif, else
if 7.5 < x <10 :
    print('Selamat nilai anda di atas rata-rata')
else:
    print('Selamat nilai anda di bawah rata-rata, silahkan belajar lagi ya GOBLOK!!!')

print('================================')
x = int(input('Masukkan Angka: ')) #Ternary operator (simple if, elif, else)
print('Nilai anda diatas kkm' if x > 10 else 'Nilai anda di bawah kkm, makanya belajar')

print('================================')
Grade = int(input('Masukkan Nilai Anda: ')) #Match case (more simple if, elif, else)
match Grade:
    case 90:
        print('Nilai Anda A')
    case 80:
        print('Nilai Anda B')
    case 70:
        print('Nilai Anda C')
    case _:
        print('Nilai Anda D, GOBLOK KOE BELAJAR ATO GA')




print('================================')
print('LOOPING') #for looping in for, while
i = 0
while i < 1: #while looping
    print('Sampai', i)
    i += 1
o = 1
while o < 3: #break 
    print('Sampai', o)
    if o == 3 :
        break
    o += 1
print('================================')
u = 0 #Stop looping 
while u < 2 :
    print('Sampai', u)
    u += 1
else:
    print('Udah sampe')  
p = 0 #Continue looping (#skip the loop) 
while p < 2 :
    print('Sampai', p)
    p += 1
    if p == 1 :
        continue
    print('Udah pak')
 
x = ['asep', 'nia', 'komang'] #for looping in for (List)
for i in x:
    print(i)

u = 'aua' #for looping in for (String)
for i in u:
    print(i)    

for i in range(2, 4, 1): #for looping in for (Range)
    print('sampai' + str(i))

for i in range(2, 6): #for looping in for (Range) continue
    print('sampai' + str(i))
    i += 1
    if i == 3:
        continue
for i in range(2, 6): #for looping in for (Range) break
    print('sampai' + str(i))
    i += 1
    if i == 3:
        break     
for i in range(2, 6): #for looping in for (Range) else
    print('sampai' + str(i))
    i += 1
else:
    print('Udah sampe')
print('================================')        

x = (   #for looping in for (List of List)
    [1, 2], 
    [3, 4], 
)
for i in x: 
    for j in i:
        print(j)



print('================================')
print('LEARN FUNCTION') #for function in def, return

def greet(): #for function in def (simple function)
    print('Hello')
greet() #call function    

def greet(name): #Parameter and argument function
    print('Hello', name + '!')
greet('Asep')

def greet(name, age): # Multiple parameter and argument function
    print('Hello', name + '!', 'You are', age, 'years old')
greet('Asep', 20)

def greet(name = 'unknown') : #Default parameter function cannot multiple
    print('Hello', name, '!')
greet()

def data_diri(name, age, hobby): #Keyword argument function
    print('Hello', name + '!')
    print('You are', age, 'years old')
    print('Your hobby is', hobby)
data_diri(
    name = 'Asep',
    age = 20,
    hobby = 'Coding'
)

def aiu(*num):  #Augumented infinity function
    print(sum(num))
aiu (1,2,3)
aiu (4,5,6)

def aiu(**std):  #Keyword argument infinity function
    print(f'My name : {std['name']}')
    print(f'My age : {std['age']}')
    print(f'My hobby : {std['hobby']}')
aiu (name = 'Asep', age = 20, hobby = 'Coding')

def uuo(x, /): #Positional-only parameter function
    print(x)
uuo(10)

def opo(*, name): #Keyword-only parameter function
    print(f'Hy my name is, {name}')
opo(name = 'Asep')

def ipi(*args):    #return function
    return sum(args)
popo = ipi(1, 10, 3)
print(f'Maka hasilnya adalah: {popo}')

def plp():  #statement function
    pass
plp()



print('=========================')
print('LAMBDA') #return value (simple)

plp = lambda nama : print(f'Hy, {nama}') #without return value
plp('asep')
plp('saipul')

popo = lambda y,z : y + z  #with return value
print(popo(2, 1))

name = input('Masukkan nama :  ')
(lambda n : print(f'Hay {n}!'))(name)

print((lambda : f'helo {name}!')())



