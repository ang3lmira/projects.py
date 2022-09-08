print("Welcome to M's UNILAG adventure!")
print("In this game you will follow me round my school, The university  of Lagos, to get some korede spag.")
print("We are about to leave the hostel, I cannot remember the directions :/")
print("Please lead the way, Try not to get us lost.")

direction_1 = input(
    "Are we going to walk to out the gate of DLI ? [yes/no] ").lower()
if direction_1 == "yes":
    print("Okay, let's go.")
    direction_2 = input("Are we getting into a cab? [yes/no] ")
    if direction_2 == "yes":
        print("Off to sports-center!")
        direction_3 = input("Are we getting into the sports center? [yes/no] ")
        if direction_3 == "no":
            print("Oh okay")
            print("Finally, some food! YUM ")
            print("Thank you babe! :)) ")
        elif direction_3 == "yes":
            print("Boss, we de go swim?")
        else:
            print("FFS! *rolls eyes* (obviously not the faculty)")
    elif direction_2 == "no":
        print("(M falls to the floor dramatically)")
        print(("M has fainted from hunger."))
    else:
        print("guy are you okay?")
elif direction_1 == "no":
    print("LOL so you want to stand outside the hostel and eat sand or?")
else:
    print("please answer me nau!")
