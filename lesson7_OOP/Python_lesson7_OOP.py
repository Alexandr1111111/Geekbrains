print('задание 1')
class Matrix():
    def __init__(self,matrix_list):
        self.shape0=len(matrix_list)
        self.shape1=len(matrix_list[0])
        self.matrix_list=matrix_list
    def __str__(self):
        print(f'matrix shape0={self.shape0}, shape1={self.shape1}')
        s_out=''
        for shape_0_data in self.matrix_list:
            shape_0_data = tuple(shape_0_data)
            s_out_shape0 = ''
            for x in shape_0_data:
                s_out_shape0=s_out_shape0+f'{x:8d}'
            s_out=s_out+'\n'+s_out_shape0 if s_out!='' else s_out_shape0
        return s_out
    def __add__(self, other):
        list_shape_0=[]
        for shape_0_data_self , shape_0_data_other in zip(self.matrix_list,other.matrix_list):
            list_sape1=[]
            for x1,x2 in zip(shape_0_data_self,shape_0_data_other):
                x=x1+x2
                list_sape1.append(x)
            list_shape_0.append(list_sape1)
        return Matrix(list_shape_0)

list=[[14,24,35],[44,54,68],[74,84,94]]
list1=[[30,40,50],[60,70,80],[90,100,160]]
M1=Matrix(list)
print(M1)
M2=Matrix(list1)
print(M2)
M3=M1+M2
print(M3)





print('')
print('задание 2')
from abc import ABC, abstractmethod
class MyAbstractClass(ABC):
    @abstractmethod
    def my_method_V(self):
        pass
    @abstractmethod
    def my_method_H(self):
        pass

class Сlothes(MyAbstractClass):
    def __init__(self,name,X):
        self.param=name
        self.name=name
        self.V=0
        self.H=0
        self.X=X
        self.result=name
    def my_method_V(self):
        return self.V/6.5 + 0.5
    def my_method_H(self):
        return 2*self.H + 0.3
    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, result):
        if result =='пальто':
            self.H = self.X
            self.__result=self.my_method_H()
        elif result=='костюм':
            self.V=self.X
            self.__result = self.my_method_V()

    @property
    def param(self):
        return self.__param

    @param.setter
    def param(self, param):
        if param == 'пальто':
            self.__param='размер'
        elif param == 'костюм':
            self.__param='рост'
    def __str__(self):
        return f'для производства {self.name} {self.param} {self.X} требуется {self.result} ткани'

p1=Сlothes('пальто',10)
print(p1)
p2=Сlothes('пальто',20)
print(p2)
p3=Сlothes('пальто',30)
print(p3)
k1=Сlothes('костюм',40)
print(k1)
k2=Сlothes('костюм',50)
print(k2)
k3=Сlothes('костюм',60)
print(k3)
result=p1.result+p2.result+p3.result+k1.result+k2.result+k3.result
print('общее количество ткани ',result,'метров')






print('')
print('задание 3')
class Organic_cells():
    def __init__(self,sum_Organic_cells):
        self.Organic_cells=sum_Organic_cells
        self.result=0
    def __add__(self, other):
        return Organic_cells(self.Organic_cells+other.Organic_cells)
    def __sub__(self, other):
        if self.Organic_cells>other.Organic_cells:
            return Organic_cells(self.Organic_cells-other.Organic_cells)
        else:print('Вычитание клеток невозможно, органических клеток в первой группе должно быть больше чем во второй')
    def __mul__(self, other):
        return Organic_cells(self.Organic_cells*other.Organic_cells)
    def __truediv__(self, other):
        return Organic_cells(int(self.Organic_cells/other.Organic_cells))
    def make_order(self,column):
        s=''
        count=0
        count_organic=0
        while(True):
            if count==column:
                s = s + '/n'
                count=-1
            else:
                s=s+'*' if self.Organic_cells!=0 else s
                count_organic += 1
            count=count+1
            if count_organic==self.Organic_cells or self.Organic_cells==0:
                break

        print(s)
    def get_var_name(self):
        for k, v in globals().items():
            if v is self:
                return k
    def __str__(self):
        return f'в классе {self.get_var_name()}, количество ячеек {self.Organic_cells}'



Organic_cells1=Organic_cells(14)
Organic_cells1.make_order(6)
print(Organic_cells1)
print('')
Organic_cells2=Organic_cells(18)
Organic_cells2.make_order(6)
print(Organic_cells2)
print('')
Organic_cells_add=Organic_cells1+Organic_cells2
Organic_cells_add.make_order(6)
print(Organic_cells_add)
print('')
Organic_cells_sub=Organic_cells1-Organic_cells2
Organic_cells_sub=Organic_cells2-Organic_cells1
Organic_cells_sub.make_order(6)
print(Organic_cells_sub)
print('')
Organic_cells_mul=Organic_cells1*Organic_cells2
Organic_cells_mul.make_order(6)
print(Organic_cells_mul)
print('')
Organic_cells_truediv=Organic_cells1/Organic_cells2
Organic_cells_truediv.make_order(6)
print(Organic_cells_truediv)
print('')
Organic_cells_truediv10=Organic_cells2/Organic_cells1
Organic_cells_truediv10.make_order(6)
print(Organic_cells_truediv10)
print('')










