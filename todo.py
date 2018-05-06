def run() -> None:
    '''The main module that prompts the user for what they wana do
    '''
    print('Menu')
    print("1) View Todo")
    print("2) Add Task")
    i = input("What would you like to do?: ")


    if i == '1':
        print(t)
    elif i == '2':
        t.add()

    run()

#future use: sometimes we say the right thing but type it wrong, this should help with that
def case_generator(s: str) -> 'List[str]':
    '''Returns list with all possible uppercase &
    lowercase combinations of string s
    Precondition: s is a lowercase string

    >>> case_generator("On")
    [on, ON, oN, oN]
    '''
    '''
    if len(s) == 0:
        return [s[0],]


    s[0] + case_generator(s[1:])
    s[0].upper() + case_generator(s[1:])
    '''

class Todo:

    def __init__(self: "Todo", size: int=0, data: dict={}):
        self.size, self.data = size, data

    def __repr__(self) -> str:
        if self.size == 0:
            return '**************************\nEmpty Todo list' + '\n**************************\n'

        s = '**************************\n'
        s += 'TODO LIST: \n'
        count = 0
        for i in self.data:
            if count == (self.size - 1):
                s += str(i) + ")" + " " + self.data[i]
            else:
                s += str(i) + ")" + " " + self.data[i] + '\n'
            count += 1
        return s + '\n**************************\n'

    def add(self) -> None:
        task = input("Enter Task: ")
        self.size += 1
        self.data[self.size] = task


if __name__ == '__main__':
    t = Todo()
    run()
