import socket
import configparser
import logging


class ACServer:

    config = configparser.ConfigParser()

    def __init__(self):
        try:
            with open("serverconfig.ini", "r") as configfile:
                self.config.read("serverconfig.ini")
        except FileNotFoundError:
            with open("serverconfig.ini", "w") as configfile:
                self.config['DEFAULT'] = {"port": "8844",
                                          "maxconnections": "128",
                                          }
                self.config.write(configfile)

        self.port = int(self.config["DEFAULT"]["port"])
        self.max_connections = int(self.config["DEFAULT"]["maxconnections"])

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self._socket.bind(("", self.port))
            self._socket.listen(self.max_connections)
        except OSError as e:
            print(e)
            exit()
