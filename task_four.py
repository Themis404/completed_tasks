'''
7.С начала суток прошло H часов,
M минут, S секунд (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60).
По данным числам H, M, S определите угол (в градусах),
на который повернулаcь часовая стрелка с начала суток
и выведите его в виде действительного числа.
'''

def time_right_now(seconds, minutes, hours, half_day):

    while seconds >= 60:
        seconds = seconds - 60
        minutes += 1
        return seconds, minutes

    while minutes >= 60:
        minutes = minutes - 60
        hours += 1
        return minutes, hours

    while hours > 12:
        hours = hours - 12
        half_day += 1
        return hours, half_day

    if hours <= 12:
        half_day += 1
        return half_day

def half_day_(half_day):

    if (half_day % 2) == 0:
        return "Это день"
    else:
        return "Это ночь/утро"

def way_into_degrees( hour_all, min_all, sec_all, seconds, minutes, hours):

    time = (hours*hour_all) + (minutes*min_all) + (seconds*sec_all)
    degrees_all = 360/(sec_all * min_all * hour_all)
    degrees = time*degrees_all
    return degrees

def main():

    half_day = 0
    sec_all = 60
    min_all = 60
    hour_all = 12

    print("Сколько времени? ")
    hours = int(input("Сколько часов: "))
    minutes = int(input("Сколько минут: "))
    seconds = int(input("Сколько секунда: "))

    time_right_now(seconds, minutes, hours, half_day)
    print("Время: часы", hours, ", минуты", minutes, ", секунды", seconds)
    print(half_day_(half_day))
    print(way_into_degrees(hour_all, min_all, sec_all, seconds, minutes, hours), "°")

if __name__ == "__main__":
    main()