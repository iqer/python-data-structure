def remove_k_digits(num, k):
    for i in range(0, k):
        for j in range(0, len(num)-1):
            if num[j] > num[j+1]:
                num = num[:j] + num[j+1:]
                break

    for j in range(0, len(num)-1):
        if num[0] != '0':
            break
        num = num[1:len(num)]

    if len(num) == 0:
        return "0"

    return num


def remove_k_digits_v2(num, k):
    new_length = len(num) - k

    stack = list()
    for i in range(len(num)):
        c = num[i]
        if len(stack) > 0 and stack[-1] > c and k > 0:
            stack.pop()
            k -= 1
        if c == '0' and len(stack) == 0:
            new_length -= 1
            if new_length <= 0:
                return '0'
            continue

        stack.append(c)

    if new_length <= 0:
        return "0"
    return ''.join(stack)


if __name__ == '__main__':
    print(remove_k_digits("1593212", 3))
    print(remove_k_digits("30200", 1))
    print(remove_k_digits("10", 2))
    print(remove_k_digits("541270396", 3))
    print(remove_k_digits("1593212", 4))
    print(remove_k_digits("1234", 1))
    print(remove_k_digits_v2("1593212", 3))
    print(remove_k_digits_v2("30200", 1))
    print(remove_k_digits_v2("10", 2))
    print(remove_k_digits_v2("541270396", 3))
    print(remove_k_digits_v2("1593212", 4))
    print(remove_k_digits_v2("1234", 1))
