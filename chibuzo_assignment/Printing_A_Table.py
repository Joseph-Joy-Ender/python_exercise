print("a             b            pow(a,b)")
print()
a = 1

for i in range(a, 6):
    a = i
    b = a + 1
    c = int(pow(a, b))
    d = "%s             %s             %s" % (str(a), str(b), str(c))
    print(d)
