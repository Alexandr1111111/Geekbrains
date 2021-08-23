print('задание1')
class Data():
    def __init__(self,data):
        Data.data=data
    @staticmethod
    def validation_data():
        dict_month={1:'январь',2:'февраль',3:'март',4:'апрель',5:'март',6:'июнь',7:'июль',8:'август',9:'сентябрь',
                    10:'ноябрь',11:'октябрь',12:'декабрь'}
        data=Data.data_to_int()
        print(f'Дата: {data[0]} {dict_month[data[1]]} {data[2]} года')


    @classmethod
    def data_to_int(cls):
        print(cls.data,cls)
        spl=cls.data.split('-')
        arr=[]
        for dat in spl:
            arr.append(int(dat))
        return arr

Data_cls=Data('20-10-2190')
Data.validation_data()

print('')
print('задание 2')
while True:
    try:
        data=int(input('Введите делитель числа 1000,  если введете 0 программа обработает исключение '))
        x=1000/data
    except ZeroDivisionError as e:
        print('ошибка деления на ноль исключение',e)
    except Exception as e:
        print(e)
    finally:
        exit = input('Введите stop чтобы выйти из программы ')
        if exit=='stop':
            break

print('')
print('задание 3')
class ExceptionTypeError(Exception):

    def __init__(self,):
        self.message = "\tИсключение несоответствующий тип данных. Для ввода используйте число "

        # переопределяется конструктор встроенного класса `Exception()`
        #super().__init__(self.message)
    def __str__(self):
        return self.message

    def inputData(self):
        arr = []
        while True:
            try:
                data = input('Введите числа по очереди или stop чтобы выйти из программы ')
                if data == 'stop':
                    print('Результат, массив: ',arr)
                    break
                try:
                    value=int(data)
                except Exception:
                    typex='str'
                else:
                    typex='value'
                    arr.append(value)
                if typex=='str':
                    raise ExceptionTypeError()

            except Exception as e:
                print(e)

arradd = ExceptionTypeError()
arradd.inputData()

print('')
print('задание 4')


class Warehouse():
    def __init__(self, number_of_cells_Office_equipment, number_truck_yards):
        self.number_of_cells_Office_equipment = number_of_cells_Office_equipment
        self.number_truck_yards = number_truck_yards


class Office_equipment():
    def __init__(self, pice=0):
        self.pice = pice
        self.Truck = self.pice

    @property
    def Truck(self):
        return self.__Truck

    @Truck.setter
    def Truck(self, Truck):
        self.__Truck = int(Truck / 50) if Truck % 50 == 0 else int(Truck / 50) + 1

    def getTruck(self):
        return self.Truck

    def get_pice(self):
        return self.pice


class PC(Office_equipment):
    def __init__(self, pice=0):
        self.__name = 'Персональный компьютер'
        super().__init__(pice=pice)

    def __str__(self):
        return f'{self.__name} количество {self.pice}'

    def get_name(self):
        return self.__name


class Notebook(Office_equipment):
    def __init__(self, pice=0):
        self.__name = 'Ноутбук'
        super().__init__(pice=pice)

    def __str__(self):
        return f'{self.__name} количество {self.pice}'

    def get_name(self):
        return self.__name


class Tablet(Office_equipment):
    def __init__(self, pice=0):
        self.__name = 'Планшет'
        super().__init__(pice=pice)

    def __str__(self):
        return f'{self.__name} количество {self.pice}'

    def get_name(self):
        return self.__name


class Servers(Office_equipment):
    def __init__(self, pice=0):
        self.__name = 'Сервер'
        super().__init__(pice=pice)

    def __str__(self):
        return f'{self.__name} количество {self.pice}'

    def get_name(self):
        return self.__name


print('')
print('задание 5')


class Warehouse():
    def __init__(self, number_of_cells_Office_equipment, number_truck_yards):
        '''

        :param number_of_cells_Office_equipment: вместимость склада в ячейках оргтехники
        :param number_truck_yards: количество свободных площадок для грузовых автомобилей
        '''
        self.number_of_cells_Office_equipment =number_of_cells_Office_equipment
        self.free_cells =self.number_of_cells_Office_equipment
        self.number_truck_yards = number_truck_yards
        self.subdivision = ['депортамент персональных компьютеров', 'депортамент ноутбуков', 'депортамент планшетов',
                            'депортамент серверов']
        self.item_Office_equipment = {'Персональный компьютер': 'депортамент персональных компьютеров',
                                      'Ноутбук': 'депортамент ноутбуков', 'Планшет': 'депортамент планшетов',
                                      'Сервер': 'депортамент серверов'}
        self.subdivision = {'депортамент персональных компьютеров': 0, 'депортамент ноутбуков': 0,
                            'депортамент планшетов': 0,
                            'депортамент серверов': 0}
        self.trucks_have_arrived = 0

    def get_place_Truck(self):
        '''
        метод возвращает количество свободных мест разгрузки грузовых автомобилей
        :return: int
        '''
        return self.number_truck_yards - self.trucks_have_arrived

    def reception_of_office_equipment(self, Office_equipment):
        '''
           метод отвечающий за прием оргтехники
        '''
        pice = Office_equipment.get_pice()
        name = Office_equipment.get_name()
        self.trucks_have_arrived = Office_equipment.Truck
        self.subdivision[self.item_Office_equipment[name]] = self.subdivision[self.item_Office_equipment[name]] + pice
        free_place = self.get_place_Truck()
        if free_place < 0:
            print('Заняты все разгрузочные площадки')
            free_place = 0
        print(
            f'Прибыл груз {name} в количестве {pice} штук занял площадок для разгрузки {Office_equipment.Truck} свободных площадок {free_place}')
        free_place_Warehouse = self.free_cells - pice  # sum([x for x in self.subdivision.values()])
        if free_place_Warehouse < 0:
            print(
                f'Склад переполнен склад вмещает {self.number_of_cells_Office_equipment} единиц оргтехники, свободных {self.free_cells}')
        else:
            print(
                f'склад вмещает {self.number_of_cells_Office_equipment} единиц оргтехники, свободно после приема груза {free_place_Warehouse}')
            print(f'Груз размещен в {self.item_Office_equipment[name]}')
            print(f'Всего на складе размещено по депортаментам', self.subdivision)
            self.free_cells = self.free_cells - pice


W = Warehouse( 1200, 8)
Servers = Servers(100)
W.reception_of_office_equipment(Servers)
print('')
PC300 = PC(300)
W.reception_of_office_equipment(PC300)
print('')
Notebook1 = Notebook(400)
W.reception_of_office_equipment(Notebook1)
print('')
Tablet400 = Tablet(400)
W.reception_of_office_equipment(Tablet400)
print('')
Tablet90 = Tablet(90)
W.reception_of_office_equipment(Tablet90)


print('')
print('задание 6 Валидация')

def Validtation(parametr,str):
    '''
    метод проверяе данные и выдает ошибку если параметр не число
    :str: наименование параметра
    :param parametr: данные для валидации
    :return: int если parametr число и  ошибку если другой тип данных
    '''
    param_output=parametr
    try:
        param_output=int(parametr)
    except Exception as e:
        print('')
        print(f'Ошибка данные параматра {str} должны быть числом')
    return param_output

class Warehouse():
    def __init__(self, number_of_cells_Office_equipment, number_truck_yards):
        '''

        :param number_of_cells_Office_equipment: вместимость склада в ячейках оргтехники
        :param number_truck_yards: количество свободных площадок для грузовых автомобилей
        '''
        self.number_of_cells_Office_equipment =Validtation(number_of_cells_Office_equipment,'number_of_cells_Office_equipment')
        self.free_cells =Validtation( self.number_of_cells_Office_equipment,'number_of_cells_Office_equipment')
        self.number_truck_yards =Validtation ( number_truck_yards,'number_truck_yards')
        self.subdivision = ['депортамент персональных компьютеров', 'депортамент ноутбуков', 'депортамент планшетов',
                            'депортамент серверов']
        self.item_Office_equipment = {'Персональный компьютер': 'депортамент персональных компьютеров',
                                      'Ноутбук': 'депортамент ноутбуков', 'Планшет': 'депортамент планшетов',
                                      'Сервер': 'депортамент серверов'}
        self.subdivision = {'депортамент персональных компьютеров': 0, 'депортамент ноутбуков': 0,
                            'депортамент планшетов': 0,
                            'депортамент серверов': 0}
        self.trucks_have_arrived = 0

    def get_place_Truck(self):
        '''
        метод возвращает количество свободных мест разгрузки грузовых автомобилей
        :return: int
        '''
        return self.number_truck_yards - self.trucks_have_arrived

    def reception_of_office_equipment(self, Office_equipment):
        '''
           метод отвечающий за прием оргтехники
        '''
        pice = Office_equipment.get_pice()
        name = Office_equipment.get_name()
        self.trucks_have_arrived = Office_equipment.Truck
        self.subdivision[self.item_Office_equipment[name]] = self.subdivision[self.item_Office_equipment[name]] + pice
        free_place = self.get_place_Truck()
        if free_place < 0:
            print('Заняты все разгрузочные площадки')
            free_place = 0
        print(
            f'Прибыл груз {name} в количестве {pice} штук занял площадок для разгрузки {Office_equipment.Truck} свободных площадок {free_place}')
        free_place_Warehouse = self.free_cells - pice  # sum([x for x in self.subdivision.values()])
        if free_place_Warehouse < 0:
            print(
                f'Склад переполнен склад вмещает {self.number_of_cells_Office_equipment} единиц оргтехники, свободных {self.free_cells}')
        else:
            print(
                f'склад вмещает {self.number_of_cells_Office_equipment} единиц оргтехники, свободно после приема груза {free_place_Warehouse}')
            print(f'Груз размещен в {self.item_Office_equipment[name]}')
            print(f'Всего на складе размещено по депортаментам', self.subdivision)
            self.free_cells = self.free_cells - pice

print('')
W = Warehouse( 1000, '10')
Notebook600 = Notebook(600)
W.reception_of_office_equipment(Notebook600)

W = Warehouse( 1000, 'srt')
Notebook900 = Notebook(900)
W.reception_of_office_equipment(Notebook900)

print('')
print('задание 6 Валидация')

class Comlex_number():
    def __init__(self,a,b,c=True):
        self.a=a
        self.b=b
        self.complex_n=complex(self.a,self.b) if c==True else a
    def __str__(self):
        return 'комплексное число'+str(self.complex_n)
    def __add__(self, other):
        return Comlex_number(self.complex_n+other.complex_n,0,c=False)
    def __mul__(self, other):
        return Comlex_number(self.complex_n*other.complex_n,0,c=False)


c1=Comlex_number(10,18)
print(c1)
c3=Comlex_number(6,14)
print(c3)
cadd=c1+c3
print(cadd)
cmul=c1*c3
print(cmul)