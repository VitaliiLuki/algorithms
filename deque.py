# id успешной отправки решения: 78879516
from exeptions import EmptyListError, ListOverflow


class Deque:
    """
    Позволяет создать массив данных(очередь) ограниченной длины(max_size).
    Поддерживает методы:
    - push_back(item) - добавляет item: int в конец очереди.(public)
    - pop_front(item) - добавляет item: int в начало очереди.(public)
    - pop_front() - возвращает и удаляет элемент из начала очереди.(public)
    - pop_back() - возвращает и удаляет элемент с конца очереди.(public)
    - is_empty() - возвращает True, если очередь пустая.(private)
    Свойства:
    - queue - показывает массив добавленных элементов.
    - size - показывает актуальную длинну массива.
    """
    def __init__(self, max_size):
        self.__queue = [None] * max_size
        self.__head = 0
        self.__tail = 0
        self.__max_queue_lenght = max_size
        self.__size = 0

    def push_back(self, item):
        if self.__size >= self.__max_queue_lenght:
            raise ListOverflow()
        self.__queue[self.__tail] = item
        self.__tail = (self.__tail + 1) % self.__max_queue_lenght
        self.__size += 1

    def pop_front(self):
        if self.__is_empty():
            raise EmptyListError()
        pop_item = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_queue_lenght
        self.__size -= 1
        return pop_item

    def push_front(self, item):
        if self.__size >= self.__max_queue_lenght:
            raise ListOverflow()
        self.__head = (self.__head - 1) % self.__max_queue_lenght
        self.__queue[self.__head] = item
        self.__size += 1

    def pop_back(self):
        if self.__is_empty():
            raise EmptyListError()
        pop_item = self.__queue[self.__tail - 1]
        self.__queue[self.__tail - 1] = None
        self.__tail = (self.__tail - 1) % self.__max_queue_lenght
        self.__size -= 1
        return pop_item

    def __is_empty(self):
        return self.__size == 0


def main():
    """
    Возвращает список удаленных элементов объекта deque: Deque().
    Если очередь пустая - при удалении возвращает 'error'.
    Если очередь заполнена - при попытке добавить новый item возвращает 'error'
    """

    file_name = 'input.txt'

    with open(file_name) as file:
        commands_num = int(file.readline())
        max_size = int(file.readline())
        deque = Deque(max_size)
        for _ in range(commands_num):
            command, *value = file.readline().split()
            try:
                result = (getattr(deque, command)(*value) if value
                          else getattr(deque, command))
                if result:
                    print(result())
            except (EmptyListError, ListOverflow):
                print('error')


if __name__ == '__main__':
    main()
