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
        
def sort_ranges(ranges):
    sorted_ranges = sorted(ranges, key=lambda x: int(x.split('-')[0]))
    return sorted_ranges

def fix_ranges(sorted_ranges):
    merged = []
    
    for r in sorted_ranges:
        start, end = map(int, r.split('-'))
        
        if not merged:
            merged.append([start, end])
            continue
        
        last_start, last_end = merged[-1]
        
        if start <= last_end + 1:   # overlap OR touching
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])
    
    return [f"{a}-{b}" for a, b in merged]




if __name__ == "__main__":
    ranges, ingredients = read_file()
    fresh_counter = 0
    """
    # Part 1
    for i in ingredients:
        ingredient = int(i)
        if is_in_range(ranges, ingredient):
            fresh_counter += 1
    print("Fresh ingredients count:", fresh_counter)
    """

    # Part 2
    merged_ranges = fix_ranges(sort_ranges(ranges))
    for i in merged_ranges:
        a, b = map(int, i.split('-'))
        fresh_counter += (b - a + 1)

    print("Total fresh ingredients:", fresh_counter)
