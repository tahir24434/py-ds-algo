"""
In earlier examples, jane, bob != bob, jane. In this example, jane, bob == bob, jane.
where they went into solution VS whether they went into solution ???

https://www.youtube.com/watch?v=J_odcqzHGqw&list=PLnfg8b9vdpLn9exZweTJx44CII1bYczuk&index=18
"""


def sublists(S):
    chosen = []
    _sublists(S, chosen)


def _sublists(S, chosen):
    if len(S) == 0:
        print(chosen)
    else:
        # Some persons are left to be picked
        # Pick one person
        # Choose and explore (with)
        chosen.append(S[0])
        _sublists(S[1:], chosen)
        chosen.pop()

        # Choose and explore (without)
        _sublists(S[1:], chosen)


def generic_permute_string(num_decisions, options, chosen):
    if num_decisions > 0:
        # Some dices are left to role
        # Handle one dice
        # For each value that dice could have
        for i in range(num_decisions):
            # Choose
            chosen.append(options[i])
            print("* %s" % chosen)
            # Explore
            generic_permute_string(len(options)-i-1, options[i+1:], chosen)
            # BackTrack
            chosen.pop()

if __name__ == "__main__":
    #l = [1, 2, 3]
    #sublists(l)
    print("****")
    l = 'abc'
    generic_permute_string(len(l), l, [])
