def my_range(start,stop,step):
    if step>0:
        while start <= stop:
            yield start
            start += step
    elif step<0:
        while start<=stop:
            yield start
            start+=step
    else:
        yield f'mumkun emas step nolga teng bulishi'
a=my_range(start=1,stop=10,step=1.1)
for i in a:
    print(i)
#range funksiyasi generatorlar orqali qildm manfiy bolgan holatda ham ishledi
