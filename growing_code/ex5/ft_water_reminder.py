
def ft_water_reminder():
    lastwater = int(input("Days since last watering: "))
    if lastwater > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
