class Foo:

    def __init__(self, value):
        print("Creating a Foo from:", value)
        self.value = 2 * value

    def clown(self, x):
        print("Clowning:", x)
        print(x * self.value)
        return x + self.value
    
def main():
    print("Clowning around now.")
    c1 = Foo(3)
    c2 = Foo(4)
    print(c1.clown(3))
    print(c2.clown(c1.clown(3)))

if __name__ == "__main__":
    main()