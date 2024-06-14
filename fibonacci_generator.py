
def fibonacci(n: int):
    index = 0
    a, b = 0, 1
    while index < n:
        yield a
        index += 1
        a, b = b, a + b
fibo = fibonacci(15)
for i in fibo:
    print(i)

#fibonacci generator orqali qilindi
"""fibonacci soni qanaqa sonlar => bu sonlar 0 dan boshlanadi
uzi va uzidan oldingi sonni bir biriga qoshib keyingi son hosil qilinadi 
va shu ketma ketlik davom etaversa fibonacci sonlari deyiladi"""