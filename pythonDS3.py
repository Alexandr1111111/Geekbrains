#задание 1
print('     Задание 1')
def delenie_a_na_b(a,b):
	# функция выполняет деление a на b
	
	# a -> int
	# b -> int
	# return -> int
	

	c=0
	try:
		c=a/b
	except ZeroDivisionError as e:
		print(e)
	return str(c)
a = int(input('     Введите число  a   '))
b=int(input('     Введите число b   '))
print('     результат деления'+delenie_a_na_b(a,b))

print('     Задание2')
def data_user(name,f_name,year,City,email,phone):
	# функция описывает данные пользователя
	
	
	# name -> string имя
	# f_name -> string фамилия
	# year -> string год
	# City -> string город
	# email -> string
	# phone -> string телефон	
	#return -> string
	
	print(f'     {name}  {f_name}  {year}  {City}  {email}  {phone}')

data_user(name='Патрик',f_name='Гранд',year='2800',City='Небраско',email='neb@google.com',phone='600400800')	

#задание 3
print('     задание 3')
a=int(input('     введите a   '))
b=int(input('     введите b   '))
c=int(input('     введите с   '))
def my_func(a,b,c):
	# функция выводит сумму наибольших двух аргументов
	# a -> int
	# b -> int
	# c -> int
	# return -> int
	
	mas=[a,b,c]
	min=a
	ind=0
	for i, x in enumerate(mas):
		if x<min:
			min=x
			ind=i
	mas.pop(ind)
	summa=sum(mas)
	print("     сумма двух наибльших чисел     ",summa)
my_func(a,b,c)

#задание 4
print('    задание 4')
x=int(input('    введите целое положительное число     '))
y=int(input('    введите степень в которую возвести x отрицательное число     '))
def sqrtf(x,y):
	# функция возводит x в степень y
	#x -> int
	#y -> int
	print('     ',x**y)
	isk=x
	for w in range (abs(y)+1):
		isk/=x
	print('     ',isk)
sqrtf(x,y)




#задание 5
print('     задание 5')
summa=0
b=True
while(b):
	x=input('     введите последовательность чисел   ')
	sp=x.split(' ')	
	mas=[]
	for x in sp:
		if x=='/n':
			b=False
			break			
		mas.append(int(x))
	summa=summa+sum(mas)
	print('     ',summa)
	
# задание 6
def int_funct(slovo):
	#  функция возвращает слово с большой буквы
	# slovo -> string
	# return -> string
	Bukv=slovo[0].upper()
	sl=Bukv
	for x in range(1,len(slovo)):
		sl=sl+slovo[x]
	return sl
x=input('     введите   строку разделенную пробелом    ')
x=x.split(' ')
res=''
for slovoo in x:
	res=res+' '+int_funct(slovoo)
print('   ',res)


		
	
	

	
	


