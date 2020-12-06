class Stack:
    items = []
    isEmpty = len(items) == 0

    def push(self, a):
        self.items.append(a)

    def pop(self):
        self.items.pop()

    def is_empty(self):
        a = True if len(self.items) == 0 else False
        print(f'Is stack empty? {a}')
        return (a)


def main():
    myStack = Stack()
    myStack.is_empty()
    print('Adding 1 into the stack')
    myStack.push(1)  # Firstly "1"
    myStack.is_empty()
    myStack.push(2)  # On top of it "2"
    myStack.push(3)  # On top of it "3"
    print(myStack.items)
    print('Removing the newesdst element on top of the stack')
    myStack.pop()  # now take away the "toppest" one
    print(myStack.items)
    myStack.pop()  # now take away the "toppest" one
    print(myStack.items)
    myStack.is_empty()
    myStack.pop()  # now take away the "toppest" one
    print(myStack.items)
    myStack.is_empty()


if __name__ == '__main__': main()
