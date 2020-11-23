def find_nearest_number(numbers):
    index = find_transfer_point(numbers)
    if index == 0:
        return None
    numbers_copy = numbers.copy()
    exchange_head(index, numbers_copy)
    reverse(index, numbers_copy)
    return numbers_copy


def find_transfer_point(numbers):
    for i in range(len(numbers)-1, 0, -1):
        if numbers[i] > numbers[i-1]:
            return i
    return 0


def exchange_head(index, numbers):
    head = numbers[index-1]
    for i in range(len(numbers)-1, 0, -1):
        if head < numbers[i]:
            numbers[index-1] = numbers[i]
            numbers[i] = head
            break
    return numbers


def reverse(index, numbers):
    i = index
    j = len(numbers) - 1
    while i < j:
        temp = numbers[i]
        numbers[i] = numbers[j]
        numbers[j] = temp
        i += 1
        j -= 1
    return numbers


def output_numbers(numbers):
    for i in numbers:
        print(i, end='')
    print()


if __name__ == '__main__':
    my_numbers = [1, 2, 3, 4, 5]
    for k in range(10):
        my_numbers = find_nearest_number(my_numbers)
        output_numbers(my_numbers)
