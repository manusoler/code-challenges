n = int(input())
words = [input() for s in range(n)]
print("\n".join(["{} {}".format(w[0::2],w[1::2]) for w in words]))