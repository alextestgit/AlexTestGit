""" if possible create palindrome
its possible in case we have 0 or 1 odd numbers."""

def test1(string):
    myset = set(string)
    tesdic={}
    for char_ in myset:
        if string.count(char_) %2:
            tesdic[char_]= string.count(char_)
    print( tesdic)
    len_ =len(tesdic)
    return  len_ <2




test = ("qwewqrwers", "aa", "aba", "abba", "12321", "1234321", "12344321", "12343211")
for a in test:
    # print(a, "\t", issimetry1(a))
    print(a, "\t", test1(a))


