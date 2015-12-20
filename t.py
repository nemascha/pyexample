# coding=utf-8


def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        for k, v in current.items():
            if isinstance(v, dict):
                if v.keys() == []:
                    result["/".join((path + (k,)))] = ""
                else:
                    stack.append((path + (k,), v))
            else:
                result["/".join((path + (k,)))] = v
    return result

if __name__ == '__main__':
    a = 2
    b = 3
    print(a + b)
    #print(flatten({"empty": {}}))
