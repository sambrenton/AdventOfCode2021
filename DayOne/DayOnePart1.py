numbers = []
increases = 0 

with open ('input.txt') as input_data:
    for lines in input_data:
        numbers.append(int(lines.strip()))

for n in range(0, len(numbers)):
    current_number = numbers[n]
    previous_number = numbers[n-1]
    if current_number > previous_number:
        increases += 1
        
print(increases)
