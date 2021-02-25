clients ='pablo,ricardo,'
labels ={
    'label1': 'client is already in the client\'s list ',
    'label2': 'client is not in client\'s list',
    'label3': 'the client {} is in the client\'s list',
    'label4': 'the client {} is not our the client\'s list'
}


def create_client(client_name):
    global clients
    global labels
    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print(labels['label1'])

def search_client(client_name):
    global clients
    clients_list = clients.split(',')

    for client in clients_list:
        if client != client_name:
            continue
        else:
            return True
    

def update_client(client_name, updated_client_name):
    global clients
    global labels
    if client_name in clients:
        clients = clients.replace(client_name + ',', updated_client_name+ ',')
    else:
        print(labels['label2'])


def delete_client(client_name):
    global clients
    global labels

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        print(labels['label2'])


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
    print('[S]earch client')

def _get_client_name(modificator=''):
    return input(f"what's the {modificator+' '}client name? ")


if __name__ == '__main__':
    _print_welcome()
    command = (input()).upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name=_get_client_name('updated' )
        update_client(client_name, update_client_name)
    elif command =='S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print(labels['label3'].format(client_name))
        else:
            print(labels['label4'].format(client_name))
    else:
        print('Invalid command')
    list_clients()
