def read_file():
    with open('puzzle_input', 'r') as f:
        return [list(line.rstrip('\n')) for line in f]
    
def count_rolls(data, x, y):
    roll_count = 0
    for a in range(-1, 2, 1):
        for b in range(-1, 2, 1):
            try:
                if a == 0 and b == 0:
                    continue

                if ((x + a) < 0 or (y + b) < 0) or ((x + a) >= len(data)) or ((y + b) >= len(data[0])):
                    continue

                if data[x + a][y + b] == '@':
                    roll_count += 1
            except:
                continue
    
    return roll_count

if __name__ == "__main__":
    lines = read_file()
    print("Roll count (0,0):", count_rolls(lines, 0, 0))

    print("Roll count (1,1):", count_rolls(lines, 1, 1))
    #print(lines[0:3])