

def mark_not_good(numbers, digit):
    result = []
    for number in numbers:
        if str(digit) in str(number):
            result.append('not_good')
        else:
            result.append(number)
    return result

 my_numbers = [1234, 5678, 9012, 3456]
 marked_numbers = mark_not_good(my_numbers, 5)
 print(marked_numbers)


def not_good_number(bad_nums):
    
    bad_nums = [1234, 1111, 0000, 1212, 7777, 1004, 2000, 4444,
                2222, 6969, 9999, 3333, 5555, 6666, 1122, 1313,
                8888, 4321, 2001, 1010, 2003, 2004, 2005, 2006,
                2007, 2008, 2009, 2010]
    for item in bad_nums:
        num = int(input('Enter a Number: '))
        if num in bad_nums:
            return True
        else:
            return False
    return bad_nums


bad_nums = [1234, 1111, 0000, 1212, 7777, 1004, 2000, 4444,
                2222, 6969, 9999, 3333, 5555, 6666, 1122, 1313,
                8888, 4321, 2001, 1010, 2003, 2004, 2005, 2006,
                2007, 2008, 2009, 2010]
result = int(input('Enter a pin: '))
if result in bad_nums:
    print('Try a different set of numbers')
else:
    print('Pin Set')

if no good:
    print('no hoood')

print('Hello')