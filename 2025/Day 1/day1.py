def read_file():
    with open("puzzle_input", "r") as f:
        data = f.read().splitlines()
        return data

def rotate(current_value, amount):
    return (current_value + amount) % 100

def count_crossings(current_value, amount):
    start_raw = current_value
    end_raw = current_value + amount

    crossings = 0

    # Moving right (increasing numbers)
    if end_raw > start_raw:
        # Count how many multiples of 100 we pass going upward
        for k in range((start_raw // 100) - 1, (end_raw // 100) + 2):
            if start_raw < k * 100 <= end_raw:
                crossings += 1

    # Moving left (decreasing numbers)
    else:
        # Count multiples of 100 we pass moving downward
        for k in range((end_raw // 100) - 1, (start_raw // 100) + 2):
            if end_raw <= k * 100 < start_raw:
                crossings += 1

    return crossings


if __name__ == "__main__":
    data = read_file()
    current_value = 50
    zero_counter = 0
    for rotation in data:
        amount = int(rotation[1:])
        if rotation[0] == "L":
            amount = -amount

        # Count all crossings before rotating
        zero_counter += count_crossings(current_value, amount)

        # Apply the rotation normally
        current_value = rotate(current_value, amount)
    

    print(zero_counter)