import sys
import subprocess

try:
    import faker
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "faker"])
    import faker
    
from faker import Faker

faker = Faker()

users = list(filter(lambda user: 18 <= user[1] <= 35, [(faker.name(), faker.random_int(18, 35)) for _ in range(100)]))
login_list = list(map(lambda user: f"{user[0].split()[0][0]}{user[0].split()[1][0]}", users))

for i, user in enumerate(users):
    print(f"{i+1}. {user[0]}, возраст: {user[1]} лет")
    
print("\nСписок логинов:")
for login in login_list:
    print(login)

