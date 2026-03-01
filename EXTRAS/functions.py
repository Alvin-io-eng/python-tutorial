def main():
    # name = values().index(0)
    # age = values().index(1)
    value = values()
    name = value[0]
    age = value[1]
    # return type(value)
    return f"Name: {name}, Age: {age}"
    # return type(value)


def values():
    name = "Alvin"
    age = 20

    return name, age

if __name__ == "__main__":
    print(main())

lis_t = [1,9,8]

