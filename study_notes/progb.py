import proga
print('Begin', __name__)


print('Defines fB')


def fB():
    print('Inside fB')
    proga.fA()


print('Calls fB')

fB()

print('End', __name__)
