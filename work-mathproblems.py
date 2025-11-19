# Maths Problems
# Author: Timmie
# 14 November

# Solving Maths Problems

#
def olympic_judging():
    """Gather scores out of 10 points from 5 judges."""
    scores = [
        "Judge 1, please enter your rating out of 10.",
        "Judge 2, please enter your rating out of 10.",
        "Judge 3, please enter your rating out of 10.",
        "Judge 4, please enter your rating out of 10.",
        "Judge 5, please enter your rating out of 10.",
    ]
    # Give the judges some instructions
    print("Enter a score out of 10 of your Olympics rating.")
    print("Please do not enter scores higher than 10, decimals are allowed.")

    total_scores = 0

    # Ask questions to the subject
    for score in scores:
        # print(scores)

        # get the judges input for each score
        average = float(input(score).strip(",?! "))

        total_scores += average

        # Print out the average hours daily

        # print("Judge 1:{} ")
        # print("Judge 2:{} ")
        # print("Judge 3:{} ")
        # print("Judge 4:{} ")
        # print("Judge 5:{} ")
    average = total_scores / len(scores)
    print(f"Your Olypic score is {average}/10.")


def main():
    # Question 1

    # Question 2
    # Olympic Judging
    # Output average scores from 5 judges
    # Each score is out of 10 points
    # Program should take 5 inputs and out put the final average score
    olympic_judging()

    # Question 3
    #


if __name__ == "__main__":
    main()
