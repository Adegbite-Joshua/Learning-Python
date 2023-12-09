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
print(very_skilled)