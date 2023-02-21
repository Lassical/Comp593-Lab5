import requests

poke_api_url = 'https://pokeapi.co/api/v2/'

def main():
      pokemon =search_for_pokemon()
      print (pokemon)
      return

def search_for_pokemon(search_term):
    """Get a list of Pokemon fomr a search term
    Args:
        search_term (str): Searches for pokemon with that name

    Returns:
        str: List of pokemon with that name
    """
    #setup header params
    header_params= {
         
    'Accept' : 'application/json'

    }

    poke_search_url = f'{poke_api_url}pokemon/{search_term}'

    print(f'Searching Poke Api for "{search_term}"...', end='')
    resp_msg = requests.get(poke_search_url, headers=header_params)
   
    
    #Check if GET request eas suggessfut
    if resp_msg.ok:
        print('Success')
        body_dict = resp_msg.json()
        poke_list = [j['ability']['name'] for j in body_dict['abilities']]

        return poke_list
    else:
        print('Failed')
        print(f'Status Code: {resp_msg.status_code} ({resp_msg.reason})')
        print(f'Reason: {resp_msg.text}')
    return


if __name__ == "__main__":
      main()