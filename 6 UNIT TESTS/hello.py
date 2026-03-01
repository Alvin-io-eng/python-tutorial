def main():
    name = input("What's your name? ")
    # hello(name)
    print(hello(name))

def hello(to="World"):
    # print("Hello, ", to)
    return f"Hello, {to}"

if __name__ == "__main__":
    main()