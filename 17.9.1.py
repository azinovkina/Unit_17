seq_of_num = list(map(int, input('Введите последовательность чисел, через пробел: ').split()))

while True:
    try:
        any_num = int(input('Введите любое целое число: '))
        break
    except:
        print("Вы ввели не целое число.")

sequence = seq_of_num + [any_num]


def num_sort():
    for i in range(len(sequence)):
        idx_min = i
        for j in range(i, len(sequence)):
            if sequence[j] < sequence[idx_min]:
                idx_min = j
        if i != idx_min:
            sequence[i], sequence[idx_min] = sequence[idx_min], sequence[i]
    return (sequence)


def binary_search(sequence, any_num, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if sequence[middle] == any_num:
        return middle
    elif any_num < sequence[middle]:
        return binary_search(sequence, any_num, left, middle - 1)
    else:
        return binary_search(sequence, any_num, middle + 1, right)


print(num_sort())
print(binary_search(sequence, any_num, 0, len(sequence)) - 1)
