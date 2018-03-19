"""
write a function diceSum similar to diceRoll, but it also accepts a desired sum and
prints only combinations that add up to exactly that sum.
https://www.youtube.com/watch?v=jHLz-9RxlhE&list=PLnfg8b9vdpLn9exZweTJx44CII1bYczuk&index=16
"""


# The following function will make many un-necessary calls. We can avoid some of
# the calls made by the function. We will implement a better function with name
# dice_sum_better. Below function is just for showing the basics of backtracking
# which is important. Please see the video given in a link.
def dice_sum(num_dices, desired_sum, chosen):
    if num_dices == 0:
        if sum(chosen) == desired_sum:
            print(chosen)
    else:
        # Some dices are left to role
        # Handle one dice
        # For each value that dice could have
        for i in range(1, 7):
            # Choose
            chosen.append(i)
            # Explore
            dice_sum(num_dices - 1, desired_sum, chosen)
            # BackTrack
            chosen.pop()


def dice_sum_better(num_dices, desired_sum, sum_so_far, chosen):
    if num_dices == 0:
        print(chosen)
    else:
        # Some dices are left to role
        # Handle one dice
        # For each value that dice could have
        for i in range(1, 7):
            # Make call only
            # If picking smallest possible values are NOT exceeding desired_sum and
            # If picking largest possible value is NOT less than desired_sum.
            if (sum_so_far + i + 1*(num_dices - 1) <= desired_sum
                    and sum_so_far + i + 6*(num_dices - 1) >= desired_sum):
                # Choose
                chosen.append(i)
                # Explore
                dice_sum(num_dices - 1, desired_sum, chosen)
                # BackTrack
                chosen.pop()


if __name__ == "__main__":
    chosen = []
    print(dice_sum(2, 10, chosen))

    print(dice_sum_better(3, 4, 0, chosen))
