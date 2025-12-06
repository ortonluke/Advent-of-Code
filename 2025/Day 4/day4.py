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
    
    return roll_count < 4

if __name__ == "__main__":
    #data = read_file()
    #print(f"Roll count: {0}, {len(data[0]) - 1}", count_rolls(data, 0, len(data[0]) - 1))
    
    data = read_file()
    total_rolls = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '@':
                if count_rolls(data, i, j):
                    total_rolls += 1

    print(f"Total rolls: {total_rolls}")
    print("-----")
    #v2, same data
    total_rolls = 0
    rolls_removed = 1
    while rolls_removed > 0:
        rolls_removed = 0
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j] == '@':
                    if count_rolls(data, i, j):
                        total_rolls += 1
                        data[i][j] = '.'
                        rolls_removed += 1
    print(f"Total rolls v2: {total_rolls}")
            

            
    
