
def char_freq(x):
    d = {}
    for i in x:
        d[i] = d.get(i, 0) + 1
    print(d)

if __name__ == __main__:
    char_freq("aaaaabbbccccop")