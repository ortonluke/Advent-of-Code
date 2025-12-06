def read_file():
    with open('puzzle_input', 'r') as f:
        data = [line.strip() for line in f.readlines()]
        ranges = []
        ingredients = []
        
        found_break = False
        break_index = 0
        while not(found_break):
            line = data.pop(0)
            if line == "":
                found_break = True
            else:
                ranges.append(line)
                break_index += 1
        
        # The remaining lines not popped are ingredients
        ingredients = data

        return ranges, ingredients

def is_in_range(ranges, ingredient):
    for i in ranges:
        minimum, maximum = map(int, i.split('-'))
        if minimum <= ingredient <= maximum:
            return True
    return False
        
    

if __name__ == "__main__":
    ranges, ingredients = read_file()
    fresh_counter = 0
    for i in ingredients:
        ingredient = int(i)
        if is_in_range(ranges, ingredient):
            fresh_counter += 1
    print("Fresh ingredients count:", fresh_counter)