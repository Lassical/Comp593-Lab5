import requests

dev_key = 'uR7yLMa0Kj4eh1HaoJ6Gcuk7N6Kzk0wR'
pastebin_api_url = 'https://pastebin.com/api/api_post.php'


def main():
    url = post_new_paste('this is the title', 'this is the body', '1M', True)
    print(f'New paste URL {url}')
    print(url)

def post_new_paste(title, body_text, expiration='1M', listed=False):
    """Post new public paste to Pastebin

    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str, optional): Paste expire date(N = never, 10M = minutes, 1H, 1D, 1W, 1Y) Defaults to '1 month'.
        listed (bool, optional): Is Paste public (True) or not (False) Defaults to False.

    Returns:
        _type_: _description_
    """

    #Settup Params for request message

    paste_params = {
        'api_dev_key': dev_key,
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name' : title,
        'api_paste_expire_date' : expiration,
        'api_paste_private' : 0 if listed else 1

    }
    resp_msg = requests.post(pastebin_api_url, data=paste_params)
    print('Sending POST request to PostBin Api...')
    
    #Check if POST request was successful
    if resp_msg.ok:
        print('Success')
        return resp_msg.text
    else:
        print('Failed')
        print(f'Status Code: {resp_msg.status_code} ({resp_msg.reason})')
        print(f'Reason: {resp_msg.text}')

        return
    

if __name__ == "__main__":
      main()