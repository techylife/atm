class ATM(object):
    def __init__(self, name, cardNumber, pinNumber, amount):
        self.name = '',
        self.cardNumber = '',
        self.pinNumber = '',
        self.amount = ''
    
    def withCash(self, amount):
        print('\033[1;31m You made a successful withdraw of Rs',amount)
    
    def depCash(self, amount) :
        print('You successfully deposited Rs',amount)

print("\033[1;32m Welcome to the ATM!")
name = input("\033[1;33m Enter your name\n")
cardNum = input("\033[1;33m Please enter your card number\n")
pinNum = input("\033[1;33m Please enter your PIN\n")
t_type = input("\033[1;33m Enter the transaction type. Type W for withdrawal and D for deposit")
amt = input("\033[1;33m Enter the amount")
cardDetails = ATM(name, cardNum, pinNum, amt)
if t_type=='W':
    cardDetails.withCash(amt)
else :
    cardDetails.depCash(amt)
print("\033[1;32m Thanks for using me :)")