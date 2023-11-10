class EmptyListError(BaseException):
    """Вызывается, при попытке удалить значения из пустого массива."""
    def __init__(self, text='Операция невозможна, список пуст!'):
        self.text = text

    def __str__(self):
        return self.text


class ListOverflow(BaseException):
    """Вызывается, при попытке добавить новый элемент в заполненный список
    ограниченного размера."""
    def __init__(self, text='Невозможно добавить значение, список заполнен.'):
        self.text = text

    def __str__(self):
        return self.text


class DataNotFound(BaseException):
    """Вызывается, при попытке извлечь данные из пустого файла."""
    def __init__(self, text='Указанный файл не содержит данных!'):
        self.text = text

    def __str__(self):
        return self.text
