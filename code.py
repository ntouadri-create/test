from datetime import datetime

print("Hello ! Il est {}.".format(datetime.now().strftime("%H:%M:%S")))

from module import obtenir_temps

print(obtenir_temps())
