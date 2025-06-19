def average(grades):
    return sum(grades.values()) / len(grades)

class_B = {
    "m": 1,
    "o": 5,
}

class_c = {
    "d": 40,
    "u": 35,
    "m": 30,
}

print(f"Average for class B: {average(class_B)}")
print(f"Average for class c: {average(class_c)}")