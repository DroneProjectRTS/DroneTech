import tello

bob = tello.Tello()

# Put tello into command mode
bob.send("command", 10)

# Send the takeoff command
bob.send("takeoff", 10)

# ----------------------------------------
# Route
# ----------------------------------------

for x in range(5):
    print ("Drone is moving forward for 100 cm.")
    bob.send("forward " + str(100), 10)

    print ("Drone is going to turn counter-clockwise 144 degrees")
    bob.send("ccw "+str(144), 5)

# ----------------------------------------

# Send the land command
bob.send("land ", 4)

# Print message
print ("Mission accomplished")

# Close the socket
bob.sock.close()
