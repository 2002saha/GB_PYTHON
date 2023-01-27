import sys
import subprocess
from random import randint
try:
    import faker
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "faker"])
    import faker  
from faker import Faker
faker = Faker()

routes = [
    {"number": 1, "stations": ["A", "B", "C"], "time": 20},
    {"number": 2, "stations": ["D", "E", "F"], "time": 40},
    {"number": 3, "stations": ["G", "H", "I"], "time": 30},
    {"number": 4, "stations": ["J", "K", "L"], "time": 35},
    {"number": 5, "stations": ["M", "N", "O"], "time": 25},
]

drivers = [
    {"name": faker.name(), "age": randint(25, 40)},
    {"name": faker.name(), "age": randint(35, 50)},
    {"name": faker.name(), "age": randint(30, 45)},
    {"name": faker.name(), "age": randint(40, 55)},
    {"name": faker.name(), "age": randint(45, 60)},
]


print("Маршруты со временем в пути менее 30 минут:")
filtered_routes = list(filter(lambda route: route["time"] < 30, routes))
for route in filtered_routes:
    print(f"Маршрут {route['number']} со временем в пути {route['time']} минут")


driver_dict = {}
for route in routes:
    driver_list = []
    for driver in drivers:
        if driver["age"] > 35:
            driver_list.append(driver["name"])
    driver_dict[route["number"]] = driver_list
print("Словарь водителей:", driver_dict)


for route in routes:
    route["passengers"] = randint(10, 20)
print("Маршруты со случайным количеством пассажиров:")
for route in routes:
    print(f"Маршрут {route['number']} с {route['passengers']} пасажиров")