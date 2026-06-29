class Visacard:
    def __init__(self,holder_name,card_number):
        self.holder_name=holder_name
        self.card_number=card_number
        
    def display_details(self) :
        print(self.holder_name)
        print(self.card_number)

    def compute_rewards(self,purchase_type,amount):
        reward=amount*0.01
        print("The Reward for VISA is :",reward)

class HPVISACARD(Visacard):
    def compute_rewards(self,purchase_type, amount):
        reward=amount*0.01
        if purchase_type=="Fuel" :
            reward+=10
        print("Reward for HPVISA is :",reward)
#INPUT
card_type=input("Enter VISA/HPVISA").strip()
if card_type not in ["VISA","HPVISA"]:
    print("Invalid Card Choice")
else :
    holder_name=input("Enter the name :").strip()
    card_number=input("Enter the card number :").strip()
    amount=float(input("Enter the Amount"))
    purchase_type=input("Enter the Purchase Type : ").strip()

    if card_type=="VISA" :
        card=Visacard(holder_name,card_number)
    else :
        card=HPVISACARD(holder_name,card_number)

    card.display_details()
    card.compute_rewards(purchase_type,amount)               