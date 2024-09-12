#gameRent functions
#Module autohr: F312575

import subscriptionManager as S
import datetime as D
import database as dat
import os

#Code below used to append the file path in order for the program to loacte the text files(Sub manager)
Mpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def rent(customer_id,game_id):
    '''
    Function to update the Rental file when a game is rented out

    Parameters:
    Customer ID
    Game ID

    Returns:
    Nothing
    '''
    file = os.path.join(Mpath, "Subscription_Info.txt")
    info = []
    info.append(customer_id)
    info.append(game_id)
    Subs = S.load_subscriptions(file_name= file)
    Y = dat.rental_data()
    rented_games = []
    i = 0
    for record in Y:
        if (record[2].strip() == '' or record[2].strip() == ' '):
            rented_games.append(record)

    for record in rented_games:
        if (record[3] == customer_id):
            i = i+ 1
    #Logic to check a customer's subcsription is still valid, the game actually exists in the store and that the game is available to be rented out       
    if ((S.check_subscription(customer_id,Subs)== True) and (dat.term_ingame(game_id)== True) and (available(game_id)!= False)): 
        # Logic to check the customer is not at their limit for games they can rent out
        if ( i < S.get_rental_limit(check_sub(customer_id))):
            dat.add_rent(info)
            print("Game was successfully rented!")
        else:
            print("Error: Customer at subscription limit")
    else :
        print("Error:Invalid subscription or invalid game ID")
        
        

                   
    
def available(game_id):
    '''
    Function to check if a game is available or has been rented out

    Parameters:
    Game ID

    Returns:
    False- If the game is not available

    '''
    records = dat.rental_data()
    for record in records:
        if len(record) >= 3 and record[0] == game_id and(record[2].strip() == '' or record[2].strip() == ' ') :
            return False

def check_sub(customer_id):
    '''
    Function to check a customer's subscription type

    Parameter:
    Customer ID

    Returns:
    Subscription type
    '''
    file = os.path.join(Mpath, "Subscription_Info.txt")
    subs = S.load_subscriptions(file_name=file)
    sub_type = subs[customer_id]["SubscriptionType"]
    return sub_type

        

if __name__=="__main__":
    #Testing the available() function
    print(available("val01"))
    #Testing the rent() function
    rent("abcd","cod01")
    #Testing the check_sub() function
    print(check_sub("abcd"))
