def item():
    while True:
        x=yield
        print(x)
a=item()
next(a)
a.send('dasturchi1')
a.send('dasturchi2')
a.send('dasturchi3')
a.send('dasturchi4')
a.send('dasturchi5')
a.send('dasturchi6')
#a=a.throw(ValueError)
#bu degani shu tariqa shungacha ishla undan keyin xatolik tashla degani
a.send('dasturchi7')
a.close()
#bu shu joyda stop qil degani
a.send('dasturchi9')
a.send('dasturchi10')

""" generator metodlari ishlatib kordim <send>,<close>,<throw>"""
