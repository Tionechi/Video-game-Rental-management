#Database handling functions
#Module autohr: F312575


import datetime as D
import os

#Code below used to append the file path in order for the program to loacte the text files
Mpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def rental_dic():
    '''
    Function to load rental data into a list of dictionaries

    Parameters:
    None

    Returns:
    A list of dictionaries of rental data
    '''
    data_list = []
    file = os.path.join(Mpath, "Rental.txt")

    with open(file, "r") as file:
        for line in file:
            fields = line.strip().split(',')
            
            entry = {
                'GameID': fields[0],
                'Rental date': fields[1],
                'Return Date': fields[2],
                'Rented customer ID': fields[3]
            }

            data_list.append(entry)

    return data_list






def game_data():
    '''
    Function to access the Game_Info file and return a list of all the records in the file

    Parameters:
    None

    Returns:
    A list containing the reocrds in the Game_Info file

    '''
    file = os.path.join(Mpath, "Game_Info.txt")
    try:
        with open(file,"r") as f:
            lines = f.readlines()
            game_data =[]
            for line in lines:
                line_items = line.strip().split(',')
                game_data.append(line_items)
        return game_data
        
    except FileNotFoundError:
        print("Error: The file could not be found")
        return game_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return game_data
        


def rental_data():
    '''
    Function to access the rental file and return a list of all the records in the file

    Parameters:
    None

    Returns:
    A list containing the reocrds in the rental file

    '''
    file = os.path.join(Mpath, "Rental.txt")
    try:
        with open(file,"r") as f:
            lines = f.readlines()
            rental_data =[]
            for line in lines:
                line_items = line.strip().split(',')
                rental_data.append(line_items)
        return rental_data
        
    except FileNotFoundError:
        print("Error: The file could not be found")
        return rental_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return rental_data



def term_Inrent(game_ID):
    '''
    Function to check if a game exists in the Rental file

    Parameters:
    
    
    Returns:
    True if game exists in the rental file
    False if the game does not exist in the rental file
    '''
    file = os.path.join(Mpath, "Rental.txt")
    try:
        with open(file, 'r') as f:
            for line in f:
                if game_ID in line:
                    return True
        return False
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return False
    except Exception as e:
        print(f"an error has occurred: {e}")


def term_ingame(game_ID):
    '''
    Function to check if a game exists in the Game_Info file

    Parameters:
    Game ID
    
    
    Returns:
    True if game exists in the rental file
    False if the game does not exist in the rental file
    '''
    file = os.path.join(Mpath, "Game_Info.txt")
    try:
        with open(file, 'r') as f:
            for line in f:
                if game_ID in line:
                    return True
        return False
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return False
    except Exception as e:
        print(f"an error has occurred: {e}")



def add_rent(my_list):
    '''
    Function to add a record to the rental file

    Parameters:
    A list containing the game id and customer id

    Returns:
    Nothing
    '''
    file = os.path.join(Mpath, "Rental.txt")
    try:
        with open(file, "a") as f:
            new_record = my_list[1] + "," + D.date.today().strftime('%d/%m/%Y') + "," + " " + "," + my_list[0] + "\n"
            f.write(new_record)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"an error has occurred: {e}")


def load_rent(records):
    '''
    Function to load a list into the rental file

    Parameters:
    List of records

    Returns:
    Nothing
    '''
    file = os.path.join(Mpath, "Rental.txt")
    with open(file, 'w') as file:
        for record in records:
            file.write(','.join(record) + '\n')
                

def load_game(records):
    '''
    Function to load a list into the game_info file

    Parameters:
    List of records

    Returns:
    Nothing

    '''
    file = os.path.join(Mpath, "Game_Info.txt")
    with open(file, 'w') as file:
        for record in records:
            file.write(','.join(record) + '\n')

if __name__=="__main__":
    #Testing game_data  function
    games = game_data()
    print(games)
    #Testing rental_data function
    print("*******************************")
    history = rental_data()
    print(history)
    #Testing term_Inrent function
    print("*******************************")
    print(term_Inrent("abcd"))
    #Testing term_ingame function
    print("*******************************")
    print(term_ingame("fifa02"))
    #Testing the rental_dic function
    print("*******************************")
    dictionary = rental_dic()
    print(dictionary)
    


