a = []
        a = map(str, s)
        a = ''.join(a)
        b = int(a) + 1
        res = [int(x) for x in str(b)]
        return res
