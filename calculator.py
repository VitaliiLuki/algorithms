# id успешной отправки: 78896004
from exeptions import DataNotFound


class Stack:
    """
    Класс - калькулятор. Произодит вычисления.
    Поддерживает методы:
    - calculate(data) - принимает на вход последовательность(data) операторов
                         и операндов.
                         Возвращает результат арифметического вычисления.
                         Пример data: ['1', '2', '+', '3', '*']
                         Пример результата выполнения функции: 9
    """
    def __init__(self):
        self.__stack = []
        self.__math_operations = {
            '-': lambda a, b: b - a,
            '+': lambda a, b: b + a,
            '/': lambda a, b: b // a,
            '*': lambda a, b: b * a,
        }

    def calculate(self, data):
        if not data:
            raise DataNotFound
        for i in data:
            if i not in self.__math_operations.keys():
                self.__stack.append(int(i))
                continue
            if len(self.__stack) >= 2:
                result = self.__math_operations[i](
                    self.__stack.pop(),
                    self.__stack.pop()
                )
                self.__stack.append(result)
        return self.__stack.pop()


def main():
    """
    Читает арифметическое выражение из файла, записанное в форме обратной
    польской нотации и показывает результат вычисления этого выражения.
    """
    file = open('input.txt')
    data = file.read().rstrip().split()

    stack = Stack()

    print(stack.calculate(data))


if __name__ == '__main__':
    main()
