def ft_count_harvest_recursive():
    day1 = int(input("Days until harvest:"))
    i = 1
    count_days(day1, i)


def count_days(days, i):
    if (i <= days):
        print("Day", i)
        i = i + 1
        count_days(days, i)
    else:
        print("Harvest time!")
