import threading
import time
import socket


class Tello():

    def _init_(self):
        # IP and port of Tello
        self.tello_address = ('192.168.0.147', 8889)

        # IP and port of local computer
        self.local_address = ('', 9000)

        # Create a UDP connection that will send the command to
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Bind to the local address and port
        self.sock.bind(self.local_address)

        # Create and start listening thread that runs in the background
        # Utilizes receive function and continuously monitor for incoming messages
        self.receiveThread = threading.Thread(target=self.receive)
        self.receiveThread.daemon = True
        self.receiveThread.start()

    # Send message to Tello and allow delay in seconds
    def send(self, message, delay):
        try:
            self.sock.sendto(message.encode(), self.tello_address)
            print ("Sending message: " + message)
        except Exception as e:
            print ("Error sending: " + str(e))

        # Delay for user-defined period of time
        time.sleep(delay)

    # Receive the message from Tello
    def receive(self):
        # continuously loop and listen for incoming message
        while True:
            # Try to receive the message otherwise print exception
            try:
                response, ip_address = self.sock.recvfrom(128)
                print ("Received message: " + response.decode(encoding='utf-8'))
            except Exception as e:
                # If there's error, close the socket and break out the loop
                self.sock.close()
                print ("Error receiving: " + str(e))
                break




