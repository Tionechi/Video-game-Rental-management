#Game Search functions
#Module autohr: F312575

import database as dat



def search_games(search_term, option):
    '''
    Searches the Game Info database for records that match the criteria term

    Parameters:
    search_term - could be game title, game id, genre, or platform
    option - 1 or 2 (1 to show all games, 2 to show only availale games based on the search term)

    Returns:
    A list containing the records that match the search term

    '''
    search_results = []
    search_term.lower()
    X = dat.game_data()
    Y = dat.rental_data()
    rented_games = []
    available_games = []
    empty = []
    for record in Y:
        if (record[2].strip() == '' or record[2].strip() == ' '):
            rented_games.append(record)
    
    try:
        for sub_list in X:
            if any(search_term in str(element).lower() for element in sub_list):
                search_results.append(sub_list)
                
        id_rental = {record[0] for record in rented_games}        
        for record in search_results:
            if (record[0] not in id_rental):
                available_games.append(record)
     
        if ( option == 1 and len(search_results) != 0 ):
            return search_results #Show all results
        
        elif (option == 2 and len(available_games) != 0 ):
            return available_games #Show only games that are available
        elif (len(search_results) == 0 or  len(search_results) == 0 ): #In the case of no results
            print("No results available")
            return empty
        else:
            print("No results available")
            return empty
        
    except FileNotFoundError:
        print("Error: The file could not be found")
        return search_results
    except Exception as e:
        print(f"An error occurred: {e}")
        return search_results
    


def search_rental(search_term):
    '''
    Searches the Game Info database for records that match the criteria term

    Parameters:
    search_term

    Returns:
    A list containing the records that match the search term

    '''
    search_results = []
    search_term.lower()
    X = dat.rental_data()
    
    try:
        for sub_list in X:
            if any(search_term in str(element).lower() for element in sub_list):
                search_results.append(sub_list)

        return search_results
    except FileNotFoundError:
        print("Error: The file could not be found")
        return search_results
    except Exception as e:
        print(f"An error occurred: {e}")
        return search_results


if __name__=="__main__":
    #Testing the search() function
    print(search_games("lol03",1))
    #Testing the search_rental() function
    print(search_rental("fifa02"))
    

    




    
