vertical_travel = 0
horizontal_travel = 0
aim = 0

with open('input.txt') as input_data:
    for line in input_data.readlines():
        insctruction = line.strip()
        direction, amount = insctruction.split(' ')
        if direction == 'forward':
            horizontal_travel += int(amount)
            vertical_travel += (int(amount) * aim)
        elif direction == 'down':
            aim += int(amount)
        elif direction == 'up':
            aim -= int(amount)

print(vertical_travel * horizontal_travel)
