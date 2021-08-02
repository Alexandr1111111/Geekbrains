print('задание 1')
try:
    with open('file1.txt','w',encoding="utf-8") as f:
        while(True):
            x=input('Введите текст построчно через Enter, для завершения ввода нажмите пустую строку:\t')
            if x=='':
                break
            f.write(x+'\n')
except Exception as e:
    print(e)
print('задание 2')
with open('text1.txt','r',encoding="utf-8") as f:
    count_line=0
    cont_lenhgt=0
    for line in f:
        print(line.strip())
        count_line+=1
        cont_lenhgt=cont_lenhgt+len(line)
    print(f'клочество строк в файле {count_line} количетво символов в файле {cont_lenhgt}')
    print('')
print('задание 3')


def mean(array):
    mean=sum(array)/len(array)
    return mean
with open('Person.txt','r',encoding='utf-8') as f:
    data=[]
    sum_salary_sl=[]
    for line in f:
        sl=line.split(' ')
        i, name, salary=sl[0],sl[1],sl[2]
        i, name, salary=i,name,int(salary.strip())
        sum_salary_sl.append(salary)
        if salary<20000:
            data.append([ name, salary])
    mean_salary=mean(sum_salary_sl)
    print(f'зарплата сотрудников ниже 20000:')
    for i,x in enumerate(data):
        print(f'\t{i+1} {x[0]} {x[1]}')
    print(f'средняя зарплата сотрудников {mean_salary}')

print('')
print('задание 4')
data=[]
with open('one_two_tree_four.txt','r',encoding='utf-8') as f:
    dictonary={'One':'один','Two':'два','Three':'три','Four':'четыре'}
    for line in f:
        spl=line.split(' ')
        line_new=dictonary[spl[0]]+spl[1]+spl[2]
        data.append(line_new)
with open('one_two_tree_four_new.txt','w',encoding='utf-8') as f:
    for x in data:
        f.write(x)
print('файл обработан и записан в новый one_two_tree_four_new.txt ')

print('')
print('задание 5')
with open('number.txt','w',encoding='utf-8') as f:
    for x in range(10):
        f.write(str(x)+' ')
with open('number.txt','r',encoding='utf-8') as f:
    data=f.read()
    data=data.strip()
    data=data.split(' ')
    list1=[]
    for x in data:
        list1.append(int(x))
    print(f'сумма чисел в файле {sum(list1)}')

print('')
print('задание 6')
with open('academic_subject.txt','r',encoding='utf-8') as f:
    data1=[]
    for line in f:
        data=line.split(' ')
        data1.append(data)
    data_new=[]
    dictonary = {}
    for items in data1:
        number=''
        name=''
        for x in items:
            #print('x',x)
            #print(x.find('(л)'))
            if x=='':
                pass
            elif x.find('(л)')!=-1:
                number=number+' '+x.replace('(л)','')
            elif x.find('(пр)') != -1:
                number = number + ' ' + x.replace('(пр)', '')
            elif x.find('(лаб)') != -1:
                number = number + ' ' + x.replace('(лаб)', '')
            elif x.find(':') != -1:
                name = x
        number=number.strip()
        number=number.split(' ')
        number=[int(x)for x in number]
        dictonary[name]=sum(number)
    print(dictonary)

print('')
print('задание 7')
with open('firm.txt','r',encoding='utf-8') as f:
    data1 = []
    for line in f:
        data=line.split()
        print(data)
        data2=[]
        for x in data:
            if x==' ':
                pass
            else: data2.append(x)
        data1.append(data2)
    dictonary={}
    summa=[]
    list1=[]
    count=0
    for x in data1:
        name,revenue,charge=x[0],x[2],x[3]
        name, revenue, charge=name,int(revenue),int(charge)
        profit=revenue-charge
        dictonary[name]=profit
        if profit<0:
            pass
        else:
            summa.append(profit)
            count=count+1
    dictonary_average_profit={}
    dictonary_average_profit['average_profit']=sum(summa)/count
    list1.append(dictonary)
    list1.append(dictonary_average_profit)
    print(list1)
import json
with open("file_firm.json", "w") as write_f:
    json.dump(list1, write_f)
with open("file_firm.json") as read_f:
    data = json.load(read_f)
print('json',data)



