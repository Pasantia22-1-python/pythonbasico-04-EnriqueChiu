from asyncore import write
import csv
import os

from clients.models import Clients

class ClientService:

    def __init__(self, table_name):
        self.table_name = table_name

    def create_client(self):
        with open(self.table_name, mode='a') as f:
            write = csv.DictWriter(f, fieldnames=Clients.schema())
            write.writerow(Clients.to_dict())

    def list_clients(self):
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f, fieldnames=Clients.schema())
            return list(reader)

    def update_client(self, update_client):
        clients = self.list_clients()
        update_clients = []
        for client in clients:
            if client['uid'] == update_client.uid:
                update_clients.append(update_client.to_dict())
            else:
                update_clients.append(client)

        self._save_to_disk(update_clients)

    def _save_to_disk(self, clients):
        tmp_table_name = self.table_name+'.tmp'
        with open(tmp_table_name) as f:
            write = csv.DictWriter(f, fieldnames=Clients.schema())
            write.writerow(clients)

        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)