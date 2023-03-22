from art import logo
# from replit import clear
#HINT: You can call clear() to clear the output in the console.
question = True
bids = {} 
while question == True:
  # clear()  
  print(logo)
  name = input("Welcome to the secret auction program.\nWhat is your name?\n")
  bid = input("What's your bid?\n$")
  other_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  question = False

  
  def new_user_bid(name_user, bid_user):
    bids[name_user] = bid_user
    print(bids)
  

  new_user_bid(name_user = name, bid_user = bid)
  
  if other_bids == "yes":
    question = True
  elif other_bids == "no":
    val = []
    for val_bid in bids.values():
      val += val_bid
    max_val = max(val)
    print
    
      
  