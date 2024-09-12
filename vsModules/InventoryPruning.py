#Inventory Pruning module
#Module autohr: F312575

import matplotlib.pyplot as plt
import feedbackManager as FM
import datetime as D
import database as dat
import numpy as np
import os

#Code below used to append the file path in order for the program to loacte the text files(feedback manager)
Mpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def avg_ratings():
    '''
    Function to display a graph of the avaerage star ratings of each game in the Game Feedback file

    Parameters:
    None

    Returns:
    Nothing, this function displays a graph
    '''
    file = os.path.join(Mpath, "Game_Feedback.txt")
    dic = FM.load_feedback(file)
    gameIDs = np.unique([i["GameID"] for i in dic])

    average_ratings = [np.mean([i["Rating"] for i in dic if i["GameID"] == gameID]) for gameID in gameIDs]

    # Sort data based on average ratings
    sorted_ratings = np.argsort(average_ratings)
    gameIDs = gameIDs[sorted_ratings]
    average_ratings = np.array(average_ratings)[sorted_ratings]


    plt.bar(gameIDs, average_ratings, color='green')
    plt.xlabel('GameID')
    plt.ylabel('Average Star Ratings')
    plt.title('Average customer ratings Graph')
    plt.show()


def rental_fre():
    '''
    Function to display a garph of how many times a game has been rented out based on the data in the Rental databse

    Parameters:
    None

    Returns:
    Nothing, this function displays a graph
    '''
    
    dic = dat.rental_dic()
    gameID_counts = {}
    for item in dic:
        gameID = item["GameID"]
        gameID_counts[gameID] = gameID_counts.get(gameID, 0) + 1

    gameIDs = list(gameID_counts.keys())
    counts = list(gameID_counts.values())

   # Sort data based on counts
    sorted_counts = np.argsort(counts) 
    gameIDs = np.array(gameIDs)[sorted_counts]
    counts = np.array(counts)[sorted_counts]

    fig, ax = plt.subplots()
    bars = ax.bar(gameIDs, counts, color='darkcyan')
    plt.xlabel('GameID')
    plt.ylabel(' Rental Frequency')
    plt.title('Rental Frequency Graph')
    plt.xticks(rotation=45, ha='right')# Rotate labels for better visibilty
    plt.tight_layout()
    
    info_text = "Ideally games that have been in the store for more \nthan 6 months with a frequency of <2 should be deleted"
    info_box_properties = dict(boxstyle='round', facecolor='grey', alpha=0.5)
    ax.annotate(info_text, xy=(0.4, 0.95), xycoords='axes fraction',
            ha='center', va='center', bbox=info_box_properties)
    
    plt.show()

def delete_game(game_id):
    '''
    Function to delete a game from the games_info file

    Parameters:
    game ID

    Returns:
    Nothing
    '''
    if (dat.term_ingame(game_id) == True): #Check if the game_id matches an existing game id
        games = dat.game_data()
        for record in games:
            if game_id == record[0] :
                games.remove(record)
        dat.load_game(games)
        print("The game was successfully deleted")
    else:
        print("Error: Game ID does not exist in file")
            
if __name__=="__main__":
    #Testing the avg_ratings function
    avg_ratings()
    rental_fre()
    delete_game("lol01")
    

