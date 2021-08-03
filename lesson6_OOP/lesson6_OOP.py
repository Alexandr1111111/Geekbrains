print('задание 1')
import time
class TrafficLight():
    __color = ['красный','желный','зеленый']

    def running(self):
        start=time.time()
        count=0
        stopWhile=0
        while(True):
            time.sleep(0.3)
            end=time.time()
            if count==0:
                print(self.__color[count])
                count = count + 1
            elif end-start>7 and count==1:
                print(self.__color[count])
                start = time.time()
                count=count+1
            elif end-start>2 and count==2:
                print(self.__color[count])
                start = time.time()
                count = count + 1
            elif end-start>10 and count==3:
                start = time.time()
                count = 0
                print('')
                stopWhile=stopWhile+1
                if stopWhile==2:
                    break

TL=TrafficLight()
TL.running()

print('')
print('задание 2')

class Road():
    def __init__(self,lenght,width):
        self._length=lenght #длинна асфальта в метрах
        self._width=width #ширина асфальта в метрах
        self.mass_of_asphalt_metr=25 #масса асфальта для покрытия 1 кг\м
        self.asphalt_thickness=5/1000 #толщина асфальта в метрах
    def mass_of_asphalt(self):
        mass_of_asphalt_result=self._length*self._width*self.mass_of_asphalt_metr*self.asphalt_thickness
        return print(f'масса асфальта длинной {self._length} метров, шириной {self._width} метров, толщиной {self.asphalt_thickness} метров, равна',mass_of_asphalt_result,'тонн')

Road_obj=Road(5000,20)
Road_obj.mass_of_asphalt()


print('')
print('задание 3')
class Worker():
    def __init__(self,name,surname,position,income):
        self.name=name
        self.surname=surname
        self.position=position
        self._income=income
class Position(Worker):
    def __init__(self,name,surname,position,income):
        super().__init__(name,surname,position,income)
    def get_full_name(self):
        return print('имя сотрудника',self.name, 'фамилия сотрудника',self.surname)
    def get_total_income(self):
        return print('доход с учетом премии',self._income["wage"]+self._income["bonus"])

dictonary_incpome={"wage": 90000, "bonus": 120000}
Position=Position('Артур','Давий','Инженер',dictonary_incpome)
Position.get_full_name()
Position.get_total_income()

print('')
print('задание 4')

class Car():
    def __init__(self,speed,color,name,is_police):
        self.speed=speed
        self.color=color
        self.name=name
        self.is_police=is_police
    def go(self):
        print(f'Машина {self.color} цвета, c названием {self.name}, начала движение со скоростью {self.speed}')
    def stop(self):
        print(f'Машина {self.color} цвета, c названием {self.name}, остановилась')
    def turn(self,direction):
        print(f'Машина {self.color} цвета, c названием {self.name}, повернула на {direction}')
    def show_speed(self):
        print(f'скорость автомобиля {self.speed}')

class TownCar(Car):
    def __init__(self,speed,color,name,is_police):
        super().__init__(speed,color,name,is_police)
    def show_speed(self):
        if self.speed>60:
            print(f'скорость автомобиля {self.speed} превышение скорости')
        else:print(f'скорость автомобиля {self.speed}')
class SportCar(Car):
    def __init__(self,speed,color,name,is_police):
        super().__init__(speed,color,name,is_police)
class WorkCar(Car):
    def __init__(self,speed,color,name,is_police):
        super().__init__(speed,color,name,is_police)
    def show_speed(self):
        if self.speed>40:
            print(f'скорость автомобиля {self.speed} превышение скорости')
        else:print(f'скорость автомобиля {self.speed}')
class PoliceCar(Car):
    def __init__(self,speed,color,name,is_police):
        super().__init__(speed,color,name,is_police)
TownCar=TownCar(70,'зеленого','Cadilac',False)
TownCar.go()
TownCar.turn('право')
TownCar.show_speed()
TownCar.stop()
print('')

SportCar=SportCar(400,'фиолетового','BMW',False)
SportCar.go()
SportCar.turn('право')
SportCar.show_speed()
SportCar.stop()
print('')

WorkCar=WorkCar(50,'бежевого','Wolkswagen',False)
WorkCar.go()
WorkCar.turn('право')
WorkCar.show_speed()
WorkCar.stop()
print('')

PoliceCar=PoliceCar(190,'бело-синего','Lada',True)
PoliceCar.go()
PoliceCar.turn('право')
PoliceCar.show_speed()
PoliceCar.stop()
print('')

print('')
print('задание 5')
class Stationery():
    def __init__(self,title):
        self.title=title
    def draw(self):
        print('Запуск отрисовки')
class Pen(Stationery):
    def __init__(self,title):
        super().__init__(title)
    def draw(self):
        print(f'Запуск отрисовки {self.title}')
class Pencil(Stationery):
    def __init__(self,title):
        super().__init__(title)
    def draw(self):
        print(f'Запуск отрисовки {self.title}')
class Handle(Stationery):
    def __init__(self,title):
        super().__init__(title)
    def draw(self):
        print(f'Запуск отрисовки {self.title}')
Pen=Pen('Ручки')
Pen.draw()
Pencil=Pencil('Карандаша')
Pencil.draw()
Handle=Handle('Маркера')
Handle.draw()


