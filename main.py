clients ='pablo,ricardo,'


def create_client(client_name):
    global clients
    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('client is already in the client\'s list ')

def update_client(client_name, updated_client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name + ',', updated_client_name+ ',')
    else:
        print('client not found')


def list_clients():
    global clients
    print(clients)    


def _add_comma():
    global clients
    clients += ','

def _print_welcome():
    print('Welcome to platzi ventas')
    print('*' * 50)
    print('what would you like to do today?')
    print('[C]reate client')
    print('[U]pdate client')  
    print('[D]elete client')

def _get_client_name(modificator=''):
    return input(f"what's the {modificator+' '}client name? ")


if __name__ == '__main__':
    _print_welcome()
    command = (input()).upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
    elif command == 'D':
        pass
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name=_get_client_name('updated' )
        update_client(client_name, update_client_name)
    else:
        print('Invalid command')
    list_clients()
