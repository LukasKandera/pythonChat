#!/usr/bin/env python3

#Popis protokolu:
#OPERACIA|sprava

#OPERACIE: LOGIN|nick
#          SENDMSG|nick|Ahoj (Nesmie obsahovat |)
#          EXIT|nick
#          USERS|nick1,nick2,...           server posiela list userov ako odpoved na spravu WHO
#          WHO|nick     klient chce zoznam users

USERS = list()
import socket as s
from threading import Thread, Lock

class ChatProtocol:
    def __init__(self, nick):
        self._nick = nick

    def login(self):
        return "LOGIN|{}".format(self._nick).encode()

    def exit(self):
        return "EXIT|{}".format(self._nick).encode()

    def send_msg(self, msg):
        return "SENDMSG|{}|{}".format(self._nick,msg).encode()

    def who(self):
        return "WHO|{}".format(self._nick).encode()

    def users(self, user_list):
        users = ""
        for user in user_list:
            users += user + ","
        if len(users) > 1:
            users = users[0:len(users)-1]
        return "USERS|{}".format(users).encode()

    def parse(self, bin_msg : bytes, user_list : list, client_sock : s.socket, lock : Lock ):
        str_msg = bin_msg.decode()
        list_msg_parts = str_msg.split("|")

        if len(list_msg_parts) > 1:
            nick = list_msg_parts[1]
        if len(list_msg_parts) > 2:
            message = list_msg_parts[2]

        if list_msg_parts[0] == "LOGIN":
            lock.acquire()
            user_list.append(nick)
            lock.release()
            print("Client '{}' has been connected.".format(nick))

        elif list_msg_parts[0] == "EXIT":
            lock.acquire()
            user_list.remove(nick)
            lock.release()
            print("Client '{}' has been disconnected.".format(nick))

        elif list_msg_parts[0] == "SENDMSG":
            print("Client {} msg: {}".format(nick, message))

        elif list_msg_parts[0] == "WHO":
            print("Client {} requested list of users.".format(nick))
            client_sock.send(self.users(user_list))

        elif list_msg_parts[0] == "USERS":
            users = nick.split(",")
            print("Logged in users: {}.".format(users))

def handle_client(client_sock, lock):
    protocol = ChatProtocol("")
    while (True):
        client_msg = client_sock.recv(100)
        protocol.parse(client_msg, USERS, client_sock, lock)
    client_sock.close()

sock = s.socket(family=s.AF_INET, type=s.SOCK_STREAM)
sock.bind(("127.0.0.1",9999))
sock.listen(10)

lock = Lock()

while(True):
    (client_sock, client_addr) = sock.accept()
    print("Connected client TCP session created: ({}:{})".format(client_addr[0], client_addr[1]))

    t = Thread(target=handle_client, args=[client_sock, lock])
    t.run()


sock.close()

