numbers = [1,2,3,4,5,6,7,8,9]

details = [
        {
            "name": "Adegbite Joshua",
            "stack": "Full Stack",
            "efficiency": 85
        },
        {
            "name": "Kolins John",
            "stack": "Front End",
            "efficiency": 70
        }
    ]

# print_number = lambda x: print(x)

# map(print_number, numbers)
for i in numbers:
    print(i, end=' ')
print()

for detail in details:
    print("{} using {} stack".format(detail["name"], detail["stack"]))

very_skilled = list(filter(lambda detail: detail["efficiency"] >= 75, details))
# print(very_skilled)


# MULTI THREADING
import threading
import time

def eat_food():
    time.sleep(3)
    print('Finished eating')

def drink_coffe():
    time.sleep(4)
    print('Finished drinking')

def read():
    time.sleep(5)
    print('Finished reading')


# eat_food()
# drink_coffe()
# read()

eat = threading.Thread(target=eat_food, args=())
eat.start()

drink = threading.Thread(target=drink_coffe, args=())
drink.start()

re = threading.Thread(target=read, args=())
re.start()

eat.join()
drink.join()
re.join()

print(threading.active_count())
print(threading.Thread())
print(time.perf_counter())