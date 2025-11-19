# Big Data
# Author: Timmie
# 17 November 2025

# Open files using Python
# Read the data in the files
# Interpret the data that we read


def main():
    # Get the file
    path = "data/sfu_best_cmpt120.csv"
    file = open(path)
    # print the first line of the file
    header_row = file.readline()

    # get information about the fav pizza place
    uncle_fatihs = 0
    club_ilia = 0
    pizza_hut = 0

    # print the rest of the lines of data
    for line in file:
        # fav pizza is in column 5 (4th ind)
        # a line is a string
        # convert the string to a list
        # split the line wherever a , is
        info = line.split(",")
        fav_pizza = info[4]

        if fav_pizza == "Uncle Fatih's":
            uncle_fatihs += 1
        elif fav_pizza == "Club Ilia":
            club_ilia += 1
        elif fav_pizza == "Pizza Hut":
            pizza_hut += 1

        # Display Results
        print(f"Uncle Fatih's Votes: {uncle_fatihs}")
        print(f"Club Ilia's Votes: {club_ilia}")
        print(f"Pizza Hut's Votes: {pizza_hut}")

    file.close()


if __name__ == "__main__":
    main()
