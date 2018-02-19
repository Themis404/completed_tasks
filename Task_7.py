'''
7.С начала суток прошло H часов,
M минут, S секунд (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60).
По данным числам H, M, S определите угол (в градусах),
на который повернулаcь часовая стрелка с начала суток
и выведите его в виде действительного числа.
'''

def time_in_the_degrees(hours, minutes, seconds, hour_all, min_all, sec_all, half_day):
    while seconds >= 60:
        minutes += 1
        seconds = seconds - 60

    while minutes >= 60:
        hours += 1
        minutes = minutes - 60

    while hours > 12:
        half_day += 1
        hours = hours - 12

    if hours <= 12:
        half_day += 1

    if (half_day % 2) == 0:
        print("afternoon")
    else:
        print("night/morning")

    print("Время: часы", hours,", минуты", minutes,", секунды", seconds)
    time = (hours*hour_all) + (minutes*min_all) + (seconds*sec_all)
    degrees_all = 360/(sec_all * min_all * hour_all)
    degrees = time*degrees_all
    print(degrees,"°")

def main():
    half_day = 0
    sec_all = 60
    min_all = 60
    hour_all = 12
    print("Сколько времени? ")
    hours = int(input("Сколько часов: "))
    minutes = int(input("Сколько минут: "))
    seconds = int(input("Сколько секунда: "))
    time_in_the_degrees(hours, minutes, seconds, hour_all, min_all, sec_all, half_day)

if __name__ == "__main__":
    main()