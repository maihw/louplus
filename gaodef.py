def high(l):
    return [i.upper() for i in l]

def test(h, l):
    return h(l)

l = ["python", "linux", "git"]
test(high, l)

lst = [1, 2, 3, 4, 5]
def square(num):
    "return the num\'s pingfang."
    return num * num
print(list(map(square, lst)))
