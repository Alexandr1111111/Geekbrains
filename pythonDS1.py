#задание 1
print('      задание 1')
a=10
b=20
c='hello'
print('     ',a,b,c)
x=int(input('      введите число   '))
s=input('      введите строку  ')
print('     ',x,s)

print('      задание 2')
import math
s=int(input('      введите время в секундах   '))
minute=int(math.floor((s%3600)/60))
chas=int(math.floor(s/3600))
ost=s%60
print(f'      {chas:02}:{minute:02}:{ost:02}')

#задание 3
print('      задание 3')
s=input('      введите число   ')
print('      sum n+nn+nnn')
str=''
sum=0
for x in range(1,4):
	str=str+s*x+'+'
	sum=sum+int(s*x)
print(f'      {str} = {sum}')

#Задание 4
print('      задание 4')
x=input('      введите целое положительное число   ')
i=0
max=0
while(True):
	if int(x[i])>max:
		max=int(x[i])
	i=i+1
	if i==len(x):
		break	
print(f'      {max}')

#задание 5
print('      задание 5')
v=int(input('      введите выручку компании   '   ))
i=int(input('      введите издержки компании   '))
if v>i:
	print('      прибыль компании составила', v-i)
	print('      рентабельность компании', v/i)
	sot=int(input('      введите численность сотрудников   '))
	
	print('      прибыль фирмы в расчете на одного сотрудника', (v-i)/sot , '$')
else:
	print('     убыток компании состовляет', abs( v-i))



	

