# id успешной отправки: 79933262


def broken_search(nums, target) -> int:
    """Запускает поиск по частично отсортированному массиву."""
    left = 0
    right = len(nums) - 1
    return binary_search(nums, target, left, right)


def binary_search(nums, target, left, right):
    """Бинарный поиск по частичто отсортированному массиву."""
    if right <= left:
        if target == nums[left]:
            return left
        return -1
    mid = (left + right) // 2
    if target == nums[mid]:
        return mid
    if target < nums[mid]:
        if target >= nums[left]:
            return binary_search(nums, target, left, mid)
        else:
            # Обрабатывает случай когда target меньше всех указателей по значению.
            if nums[mid] < nums[right]: 
                # Пример [20,25,30,1,6,7,8,10,15] если target == 1, nums[mid] == 6
                # Проверка: nums[mid] < nums[right] показывает, что target справа от mid.
                return binary_search(nums, target, left, mid)
            else:
                # Пример [80,90,100,110,10,20,30,40] если target == 10, nums[mid] == 110
                # Проверка: nums[mid] >= nums[right] показывает, что target справа от mid.
                return binary_search(nums, target, mid + 1, right)
    if target > nums[mid]:
        if target <= nums[right]:
            return binary_search(nums, target, mid + 1, right)
        else:
            # Обрабатывает случай когда target больше всех указателей по значению.
            if nums[mid] < nums[right]:
                # Пример [50,60,70,10,15,20,25] если target == 70, nums[mid] == 10
                # Проверка: nums[mid] < nums[right] показывает, что target справа от mid.
                return binary_search(nums, target, left, mid)
            else:
                # Пример [80,90,100,110,20,30] если target == 110, nums[mid] == 100
                # Проверка: nums[mid] < nums[right] показывает, что target справа от mid.
                return binary_search(nums, target, mid + 1, right)


def read_file():
    """
    Читает данные из файла и возвращает массив и число для поиска в массиве.
    """
    file = open('input.txt')
    _ = file.readline()
    target = int(file.readline())
    arr = [int(i) for i in file.readline().rstrip().split()]
    return arr, target


if __name__ == '__main__':
    arr, target = read_file()
    print(broken_search(arr, target))
