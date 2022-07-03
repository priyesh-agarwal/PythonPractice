from os import system, name
gravel = r'''

                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\
'''

def main():
    print(gravel)
    print("Welcome to the Secret Auction Programme\n")
    bids = dict()
    while True:
        name = input("What's your name? ")
        bid = float(input("How much would you like to bid? $"))
        bids[name] = bid
        more_bidders = input("Are there any more bidders ? (Yes/No)").lower()
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for linux, mac
        else:
            _ = system('clear')
        if more_bidders == "no":
            break

    highest_bidder = None
    for bidder in bids:
        if highest_bidder is None or bids[bidder] > bids[highest_bidder]:
            highest_bidder = bidder

    print(f"The winner is {highest_bidder} with a bid of {bids[highest_bidder]}")

if __name__ == '__main__':
    main()