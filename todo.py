def run() -> None:
    '''The main module that prompts the user for what they wana do
    '''
    print("1) View Todo")
    print("2) Add Task")
    print("1) View Todo")
    i = input("What would you like to do?: ")


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

    def __init__(self: "Todo", size: int, data: dict={}):
        self.size, self.data = size, data

    def __repr__(self) -> str:
        s = ''
        count = 0
        for i in self.data:
            if count == (self.size - 1):
                s += str(i) + ")" + " " + self.data[i]
            else:
                s += str(i) + ")" + " " + self.data[i] + '\n'
            count += 1
        return s


if __name__ == '__main__':
    run()
