class Calculator:
    def __init__(self):
        print("Calc Init")

    def add(self, x, y):
        return x + y


def main():
    c = Calculator()
    print(c.add(10, 20))


if __name__=='__main__':
    main()