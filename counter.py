from collections import Counter
import re
path = "/usr/lib/python3.5/LICENSE.txt"
words = re.findall("\w+",open(path).read().lower())
print(Counter(words).most_common(10))

c = Counter(a=4, b=2, c=0, d=-2)
print(list(c.elements()))

print(Counter("abracadabra").most_common(3))


