def issimetry(input):
    return input == input[::-1]


def issimetry1(input):
    count, start, end = int(len(input) )/ 2, 0, -1
    while start < count:
        if input[start] == input[end]:
            start += 1
            end -= 1
        else:
            return False
    return True


def test1(string):
    return string ==  ''.join(reversed(string))



test = ("qwewqrwer", "aa", "aba", "abba", "12321", "1234321", "12344321", "12343211")
for a in test:
    # print(a, "\t", issimetry1(a))
    print(a, "\t", test1(a))
