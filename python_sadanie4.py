print('\tзадание2')
from functools import reduce
from random import  randint

list_start=[300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list_1=[ randint(0, 1000) for x in range(randint(10,16))]
result=[]
def compare1(a,b):
	'''функция выполняется в методе reduce и выполняет сравнение предыдущего значения с текущим, если текущее больше, то оно добавляется в результирующий массив
	a-> int предыдущее значение
	b-> int текущее значение
	result -> list внешний результирующий список'''
	if b > a:
		result.append(b)
	return b

		
reduce(compare1,list_1)
print('\t',list_1)
print('\t числа больше предыдущего', result)



print('')
print('\tзадание 3')
print(' \t числа кратные 21 из заданного масива   ',[x for x in range(20,240) if x%21==0])

print('')
print('\tзадание 4')
import numpy as np

def concatinate(x1,x2):
	res=[]
	res.extend(x1)
	res.extend(x2)
	return res

list_1=[ randint(0, 20) for x in range(randint(10,20))]
list_start=[2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print('\t',list_1)
result=[x for i, x in enumerate(list_1) if x not in concatinate(list_1[:i],list_1[i+1:])]
print('\tнеповторяющиеся числа',result)

print('')
print('\tзадание5')
x=[x for x in range(100,1001) if x%2==0]
def sum_reduce(x1,x2):
	return x1+x2
print('\tсумма положительных чисел',reduce(sum_reduce,x))
print('\tcheck',sum(x))

print('')
print('\tзадание6')
from itertools import count,cycle

for x in count(3):
   if x==10:
   	break
   print('\tитератор count',x)
print('')
count1=0
for x in cycle(['D','u','c','k']):
	if x=='D':
		count1+=1
	if count1==3:
		break
	print('\tитератор cycle',x)
	
print('')
print('\tзадание7')
print('\tУважаемая Александра, к сожалению не понял структуру задания, поэтому решаю интуитивно. Ошибки относительно обработки ввода, латиницы, комментариев исправил, приятного просмотра')
def factorial(n):
	'''функция считает факториал числа
	  n->int число факториал которого нужно посчитать
	  return ->  int'''
	if n==0:
		return 0
	permul=1
	for x in range(1,n+1):
		permul*=x
	return permul
				
def generator(n):
	for x in range(n):
		yield x
		
def fact(n):
	'''функция возвращает список факториалов чисел, сгенерированных генератором 
	n -> int числа генерируемые генератором от 0 до n
	return -> list'''
	res=[]
	g=generator(n)
	for x in g:
	     res.append(factorial(x))
	return res
	
while (True):
	try:	
		n=int(input('\tведите положительное число\t'))
		if n>0:
			break
	except Exception as e:
		pass
		

for i,x in enumerate(fact(n)):
	print('\t факториал числа', i,'равен',x)
	


		
