digit_names = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def day01(input):
    # Your code here
    lines = input.splitlines()   
    total1 = 0
    total2 = 0
    for line in lines:
        digits = [char for char in line if char.isnumeric()]
        if digits:
            total1 += int(digits[0]+digits[-1]) 
        digits = [char for char in translate(line) if char.isnumeric()]
        total2 += int(digits[0]+digits[-1])
    return total1, total2

def translate(line):
    for num, name in enumerate(digit_names):
        line = line.replace(name, f"{name}{num}{name}")
    return line

def main():
    input = open("input.txt").read()
    part1, part2 = day01(input)
    print("Part 1:", part1)
    print("Part 2:", part2)

if __name__ == "__main__":
    main()