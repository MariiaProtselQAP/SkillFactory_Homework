array = [int(x) for x in input("Введите последовательность чисел через пробел: ").split()]


def sort_data(array):
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left = sort_data(array[:middle])
        right = sort_data(array[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

array = sort_data(array)
print(array)

while True:
    try:
        user_number = int(input("Введите любое число из последовательности: "))
        if user_number < min(array) or user_number > max(array):
            print("Данное число не входит в список")
        break
    except ValueError:
        print("Необходимо ввести число")


def binary_search(array, user_number, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == user_number:
        return middle
    elif user_number < array[middle]:

        return binary_search(array, user_number, left, middle - 1)
    else:
        return binary_search(array, user_number, middle + 1, right)


print(binary_search(array, user_number, 0, len(array)-1))