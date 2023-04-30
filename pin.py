
def good_or_not(pin):
    
    if pin == 1234:
        print('no good')
    else:
        print('good pin')

pin = int(input('Enter a pin: '))
good_or_not(pin)

