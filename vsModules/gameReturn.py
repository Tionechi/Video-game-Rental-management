#Functions to carry out the game returning procedures
#Module autohr: F312575

import database as dat
import datetime as D
import feedbackManager as F
import os

#Code below used to append the file path in order for the program to loacte the text files(feedback manager)
Mpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
 

def return_game(game_id):
    '''
    Function to carry out the returning process and update the rental database

    Parameters:
    Game ID

    Returns:
    Nothing

    '''
    file = os.path.join(Mpath, "Game_Feedback.txt")
    records = dat.rental_data()
    for record in records:
        if len(record) >= 3 and record[0] == game_id and(record[2].strip() == '' or record[2].strip() == ' ') :
            record[2] = str(D.date.today().strftime('%d/%m/%Y'))  # Insert the date into the empty return field 
            dat.load_rent(records)
            print("DONE!")
            
    rating = int(input("Please provide a game rating out of 5 (1 - 5):"))
    comments = str(input("Provide an optional comment, if not press enter:"))
    F.add_feedback(game_id, rating, comments,file) 

if __name__=="__main__":
    #Testing the return_game() function 
    return_game("val01")
