'''
7.С начала суток прошло H часов,
M минут, S секунд (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60).
По данным числам H, M, S определите угол (в градусах),
на который повернулаcь часовая стрелка с начала суток
и выведите его в виде действительного числа.
'''

def time_sec(time):

    while time["seconds"] >= 60:
        time["seconds"] = time["seconds"] - 60
        time["minutes"] += 1


def time_min(time):

    while time["minutes"] >= 60:
        time["minutes"] = time["minutes"] - 60
        time["hours"] += 1


def time_hours(time, half_day):

    while time["hours"] > 12:
        time["hours"] = time["hours"] - 12
        half_day += 1


def time_half_day(half_day, time):

    if time["hours"] <= 12:
        half_day += 1
    return half_day

def half_day_(half_day):

    if (half_day % 2) == 0:
        return "Это день"
    else:
        return "Это ночь/утро"

def way_into_degrees( hour_all, min_all, sec_all, time):

    all_time = (time["hours"]*hour_all) + (time["minutes"]*min_all) + (time["seconds"]*sec_all)
    degrees_all = 360/(sec_all * min_all * hour_all)
    degrees = all_time*degrees_all
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
    time = {"hours": hours, "minutes": minutes, "seconds": seconds}

    time_sec(time)
    time_min(time)
    time_hours(time, half_day)

    half_day = time_half_day(half_day, time)

    print("Время: часы", time["hours"], ", минуты", time["minutes"], ", секунды", time["seconds"])
    print(half_day_(half_day))
    print(way_into_degrees(hour_all, min_all, sec_all, time), "°")

if __name__ == "__main__":
    main()