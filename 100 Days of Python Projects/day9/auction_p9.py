from art import logo
print(logo)

def find_highest_bidder(bidding_dict):
    highest_bid = 0
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with the highest bid of ${highest_bid}")



saved_info = {}
continue_bidding = True
while continue_bidding:
    print("Welcome to the secret auction program.")
    name = input("What's your name: ")
    bid = int(input("What's your bid: $"))
    saved_info[name] = bid

    more_bid = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if more_bid == "no":
        continue_bidding = False
        find_highest_bidder(saved_info)
    elif more_bid == "yes":
        print("\n" *100)