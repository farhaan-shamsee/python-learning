import os

os.system('cls')


# biding_details = {"name": "", "bid": ""}
biding_details = {}


def highest_bid(bids):
    highest_bid = 0
    winner = ''
    for value in bids:
        if bids[value] > highest_bid:
            highest_bid = bids[value]
            winner = value

    print(f"The highest bidder was {winner} with bid: {highest_bid} ")


def my_bid(name, bid):
    biding_details[name] = bid


isBid = True

while isBid:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    if input("Are there any other bidders? Type 'yes' or 'no'.\n") == "no":
        isBid = False
        my_bid(name, bid)
        highest_bid(biding_details)
    else:
        my_bid(name, bid)


print(biding_details)
