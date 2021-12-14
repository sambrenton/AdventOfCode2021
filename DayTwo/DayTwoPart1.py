vertical_travel = 0
horizontal_travel = 0

with open('input.txt') as input_data:
    for line in input_data.readlines():
        insctruction = line.strip()
        direction, amount = insctruction.split(' ')
        if direction == 'forward':
            horizontal_travel += int(amount)
        elif direction == 'down':
            vertical_travel += int(amount)
        elif direction == 'up':
            vertical_travel -= int(amount)

print(vertical_travel * horizontal_travel)
