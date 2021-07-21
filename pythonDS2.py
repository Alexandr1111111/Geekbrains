#задание 1
print('     задание 1')
x=(10,20)
x1=dict()
x1[ 'p']=10
spisok_el=[ 'строка',10,50.5,True,[400],x,x1]
for x in spisok_el:
	print('     ',type(x),'element',x)
	
print('     задание 2')
spisok=input('     введите массив чисел через пробел     ')
spisok= spisok.split(' ')
sp=[]
for x in spisok:
	sp.append(int(x))
print('     ',sp)
mas=[]
for i,x in enumerate(sp):
    d=len(sp)    
    if d==( i+1) and ( i%2==0):
    	    	mas.append(x)
    	    	break  	    	
    if i%2==0:
        mas.append(sp[i+1])
    else:
    	mas.append( sp[i-1])
print('     ',mas)

#задание 3
print('     задание 3')
x=int(input('     введите номер месяца    '))
vg=['зима', 'весна', 'лето', 'осень']
if x<3 and x>0 or x==12:
	print('     ', vg[0])
elif x>2 and x<6:
	print('     ', vg[1])
elif x>5 and x<9:
	print('     ', vg[2])
elif x>8  and x<12:
	print ('     ', vg[3])
dic={1:'зима',2:'весна',3:'лето',4:'осень'}
if x<3 and x>0 or x==12:
	print('     ', dic[1])
elif x>2 and x<6:
	print('     ', dic[2])
elif x>5 and x<9:
	print('     ', dic[3])
elif x>8  and x<12:
	print ('     ', dic[4])

#задание 4
print('задание 4')
x=input('     введите строку     ')
x=x.split()
for slovo in x:
	if len(slovo)>10:
		print(slovo[:10])
	else: print(slovo)

# задание 5
print('     заданте 5')
Reiting=[1,6,8,19,16,40]
x=int(input('     введите число     '))
Reiting.append(x)
Reiting.sort()
print('     рэйтинг',Reiting)

#задание 6
print('     задание 6')
spisok=[]
while(True):
	pos=len(spisok)
	nazvanie=input('     введите название товара     ')
	cena=input('     введите цену товара     ')
	kol=input('     введите количество товара     ')
	ed_ism=input( '     введите ед. изм. товара       ')
	end=int(input('     введите 0 если закончить ввод данных и вывести результат или 1 если продолжить ввод данных     '))
	dictl={'название':nazvanie,'цена':cena,'количество':kol,'ед':ed_ism}
	k=(pos,dictl)
	spisok.append(k)
	if end==0:
		break
print(spisok)










