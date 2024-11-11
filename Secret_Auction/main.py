from art import logo
print(logo)

def find_highest_bidder(bidders_record):
    highest_bid=0
    highest_bidder=" "
    for bidder in bidders_record:
        if bidders_record[bidder]>highest_bid:
            highest_bid=bidders_record[bidder]
            highest_bidder=bidder
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")



bidders={}
other_bidders="yes"

while other_bidders!="no":
    name=input("What is your name?")
    bid=int(input("What is your bid?"))
    other_bidders=input("Are there any othere bidders 'yes' or 'no'").lower()
    if other_bidders=="yes":
        print("\n" * 100)
    bidders[name]=bid
find_highest_bidder(bidders)



