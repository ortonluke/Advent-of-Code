def read_file():
    with open("puzzle_input", "r") as f:
        data = f.read().splitlines()
        return data

def rotate(current_value, amount):
    return (current_value + amount) % 100

def count_crossings(current_value, amount):
    size = 100
    crossings = abs(amount) // size

    # Check partial crossing
    remainder = amount % size
    if amount < 0:
        remainder = -((-amount) % size)

    new_value = (current_value + remainder) % size

    # If rotating right and wrap-around happens
    if amount > 0 and new_value < current_value:
        crossings += 1

    # If rotating left and wrap-around happens
    if amount < 0 and new_value > current_value:
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
        

        if current_value == 0:
            zero_counter += 1

    print(zero_counter)