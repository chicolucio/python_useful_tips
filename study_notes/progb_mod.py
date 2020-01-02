import proga_mod
print('Begin', __name__)


print('Defines fB')


def fB():
    print('Inside fB')
    proga_mod.fA()


print('Calls fB')

fB()

print('End', __name__)
