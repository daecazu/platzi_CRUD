import sys
import csv
import os
#Constants and variables
CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name','company','email','position']
clients =[]
labels ={
    'label1': 'client is already in the client\'s list ',
    'label2': 'client is not in client\'s list',
    'label3': 'the client {} is in the client\'s list',
    'label4': 'the client {} is not in the client\'s list',
    'label5': 'client deleted'
}

def _initialize_clients_from_storage():
    global clients
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)
        for row in reader:
            clients.append(row)

def _save_clients_to_storage():
    global clients
    tmp_table_name = f'{CLIENT_TABLE}.tmp'
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)
        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)


def create_client(client):
    global clients
    global labels
    if client not in clients:
        clients.append(client)
    else:
        print(labels['label1'])

def get_client():
    client ={
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
    return client

def search_by_name(client_name):
    global clients
    for idx, client in enumerate(clients):
        if client['name'] != client_name:
            pass
        else:
            return idx

def update_client(client_name, updated_client):
    global clients
    global labels
    idx = search_by_name(client_name)
    if idx is not None:
        clients[idx]=updated_client
    else: 
        print(labels['label4']).format(client_name)


def delete_client(client_name):
    global clients
    global labels
    idx = search_by_name(client_name)
    if idx is not None:
        del clients[idx]
        print(labels['label5'])
    else:
        print(labels['label2'])


def list_clients():
    global clients
    print('uid | name | company | email | position ')
    print('*' * 50)
    for idx, client in enumerate(clients):
        print(
            f'{idx} |'
            f' {client["name"]} |'
            f' {client["company"]} |'
            f' {client["email"]} |'
            f' {client["position"]}'
        )


def _print_welcome():
    print('Welcome to platzi ventas')
    print('*' * 50)
    print('what would you like to do today?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')  
    print('[D]elete client')
    print('[S]earch client')

def _get_client_field(field_name):
    field= None
    while not field:
        field = input(f"what's the client {field_name}? ")
    return field

if __name__ == '__main__':
    _initialize_clients_from_storage()
    _print_welcome()
    command = (input()).upper()

    if command == 'C':
        client =get_client()
        create_client(client)
    elif command == 'D':
        client_name = _get_client_field('name')
        delete_client(client_name)
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_name = _get_client_field('name to update')
        updated_client=get_client()
        update_client(client_name, updated_client)
    elif command =='S':
        client_name = _get_client_field('name')
        found = search_by_name(client_name)
        if found is not None:
            print(labels['label3'].format(client_name))
        else:
            print(labels['label4'].format(client_name))
    else:
        print('Invalid command')
    _save_clients_to_storage()
