def permute_string(string):
    chosen = ""
    _permute_string(len(string), string, chosen)


def _permute_string(str_len, string, chosen):
    if str_len == 0:
        # Base case
        print(chosen)
    else:
        # Some dices are left to role
        # Handle one dice
        # For each value that dice could have
        for i in range(str_len):
            # Choose
            chosen += string[i]
            # Explore
            _permute_string(str_len-1, string[:i]+string[i+1:], chosen)
            # BackTrack
            chosen = chosen[:-1]


def generic_permute_string(num_decisions, options, chosen):
    if num_decisions == 0:
        # Base case
        print(chosen)
    else:
        # Some dices are left to role
        # Handle one dice
        # For each value that dice could have
        for i in range(num_decisions):
            # Choose
            chosen.append(options[i])
            # Explore
            generic_permute_string(num_decisions-1, options[:i]+options[i+1:], chosen)
            # BackTrack
            chosen.pop()


if __name__ == "__main__":
    print(permute_string("abc"))
    print("***")
    generic_permute_string(len("abc"), "abc", [])
