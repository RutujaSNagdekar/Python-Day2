def d1(func):
    def w1():
       return f"Its fun with "+ func() + " always"
    return w1

def d2(func):
    def w2():
        return f"Its worst with "+ func() + " always"
    return w2


@d1
def who():
    return 'Dheeraj'
print(who())

@d2
def who():
    return 'Natasha'
print(who())


@d1
@d2
def who():
    return 'Munni'
print(who())
