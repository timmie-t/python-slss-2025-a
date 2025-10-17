# Work - McDoBot
# Author: Timmie
# 6 October

# It asks if you want fries with your meal.
fries = input("Would you like fries with your meal? ")

# It should accept Yes/yes or No/no
# as inputs, and reply appropriately depending on the answer.
if fries.lower() == "yes":
    print("A large fry is added to your cart.")

elif fries.lower() == "no":
    print("Here is your meal without fries.")

# If the user inputs anything else, it should repeat back their answer and
# say that it does not understand.
else:
    print("Sorry, I don't understand what you mean.")
