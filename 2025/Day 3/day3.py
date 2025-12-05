def read_file():
    with open('puzzle_input', 'r') as f:
        return [line.strip() for line in f.readlines()]
    
def find_highest_charge(line : str):
    first_digit = max(line[:-1])
    fd_index = line.index(str(first_digit))
    second_digit = max(line[fd_index + 1:])
    combined_value = str(first_digit) + str(second_digit)
    return int(combined_value)

def find_highest_static_charge(line : str, result = ""):
    if len(result) == 12:
        return int(result)
    back_index = len(line) - (11 - len(result))

    digit = max(line[:back_index])
    result += str(digit)

    digit_index = line[:back_index].index(str(digit))
    return find_highest_static_charge(line[digit_index + 1:], result)

if __name__ == "__main__":
    data = read_file()

    charges = [find_highest_charge(line) for line in data]
    #print(f"sum of charges (1): {sum(charges)}")

    # second part
    charges_2 = [find_highest_static_charge(line) for line in data]
    print(f"data[0]: {data[0]}")
    print(f"sum of charges (2): {sum(charges_2)}")