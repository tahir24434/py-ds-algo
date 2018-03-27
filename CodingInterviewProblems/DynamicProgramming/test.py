def is_exactly_one_repeating(l):
    count = {}
    for item in l:
        count[item] = count.get(item, 0) + 1
    repeating = False
    for val in count.values():
        if (not repeating) and (val > 1):
            repeating = True
        elif repeating and val > 1:
            return False
    return repeating


def generic_permute_string(num_decisions, options, chosen, k, res):
    if k == 0:
        # Base case
        print(chosen)
        if is_exactly_one_repeating(chosen):
            res.add(''.join(chosen))
    else:
        # Some dices are left to role
        # Handle one dice
        # For each value that dice could have
        for i in range(num_decisions):
            # Choose
            chosen.append(options[i])
            # Explore
            generic_permute_string(num_decisions-1, options[:i]+options[i+1:],
                                   chosen, k-1, res)
            # BackTrack
            chosen.pop()


if __name__ == "__main__":
    a = "abcadfg"
    k = 3
    chosen = []
    res = set()
    generic_permute_string(len(a), a, chosen, k, res)
    print(res)
