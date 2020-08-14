fahrenheit = 0
print("fahrenheit celsius")
while fahrenheit <= 250:
    celsius = (fahrenheit - 32) / 1.8
    print("{:5d} {:7.2f}".format(fahrenheit,celsius))
#{5:5d}yisishi 5ge zifu kuandu de zhengshu,{:7.2f}yisi shi
#tihuan wei 7 ge zifu kuandu de baoliu liangwei de xiaoshu
    fahrenheit = fahrenheit + 25
