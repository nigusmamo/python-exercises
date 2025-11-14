import random

first_names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
last_names = ["Smith", "Jones", "Williams", "Brown", "Davis"]

for i in range(1,51):
    random_first = random.choice(first_names)
    random_last = random.choice(last_names)
    random_name = f"{random_first} {random_last}"

    print(random_name)
