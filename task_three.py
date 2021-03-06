'''
4.Длина Московской кольцевой автомобильной дороги —109 километров.
Стартуем с нулевого километра МКАД и едем со скоростью V километров в час.
На какой отметке остановимся через T часов?
Программа получает на вход значение V и T.
Если V>0, то движемся в положительном направлении по МКАД,
если же значение V<0, то в отрицательном.
Программа должна вывести целое число от 0 до 108 — номер отметки,
на которой остановимся.
'''

def stop_road(speed, time, road):
    moment_road = abs(speed * time)
    while moment_road >= road:
        moment_road = moment_road - road
    return moment_road

def main():
    road = 109
    speed = int(input("Enter the speed of your car: "))
    time = int(input("How many hours your car will drive"))
    if speed > 0:
        print("Your car will go clockwise ")
        print(stop_road(speed, time, road))
    elif speed == 0:
        print("Your car doesn't go")
        print(stop_road(speed, time, road))
    else:
        print("Your car will go counterclockwise")
        print(stop_road(speed, time, road))

if __name__ == '__main__':
    main()




