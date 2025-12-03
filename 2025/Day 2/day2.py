def read_file():
    with open("puzzle_input", "r") as f:
        data = f.read().split(",")
        return data

def count_invalid_ids(min, max):
    min_str = str(min)
    max_str = str(max)

    invalid_ids = []

    # only generate numbers with lengths POSSIBLE within range
    for total_len in range(len(min_str), len(max_str) + 1):

        for block_len in range(1, total_len):

            # total_len must be block_len * k
            if total_len % block_len != 0:
                continue

            k = total_len // block_len
            if k < 2:
                continue

            # block must not have a leading zero
            start = 10 ** (block_len - 1)
            end = 10 ** block_len

            for block in range(start, end):
                s = str(block) * k

                # IMPORTANT: do not convert to int until after confirming length!
                if len(s) != total_len:
                    continue

                candidate = int(s)

                if candidate > max:
                    break
                if candidate >= min:
                    invalid_ids.append(candidate)

    return invalid_ids


if __name__ == "__main__":
    data = read_file()
    print(data[0:10], end="\n")

    invalid_ids = []
    for idRange in data:
        min, max = map(int, idRange.split("-"))
        results = count_invalid_ids(min, max)
        for r in results:
            invalid_ids.append(r)
    print(f"Total invalid IDs: {sum(invalid_ids)}")

    
        
