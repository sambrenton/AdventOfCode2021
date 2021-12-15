def get_count(n):
    zero_count = 0
    one_count = 0
    with open('input.txt') as input_data:
        for line in input_data.readlines():
            digit = int(line.strip()[n])
            if digit == 0:
                zero_count += 1
            if digit == 1:
                one_count += 1
        if zero_count > one_count:
            return 0
        else:
            return 1

def get_binary():
    value = ''
    value2 = ''
    for i in range (0, 12):
        value = value+str(get_count(i))
    return value

decimal1 = (int(get_binary(), base=2))
decimal2 = ''

for bit in get_binary():
    if bit == '0':
        decimal2 = decimal2+'1'
    if bit == '1':
        decimal2 = decimal2+'0'

print(decimal1 * int(decimal2, base=2))
