import tello

bob = tello.Tello()

# Put tello into command mode
bob.send("command", 10)

# Send the takeoff command
bob.send("takeoff", 10)

# ----------------------------------------
# Route
# ----------------------------------------

# Route A to B
print ("Drone is moving forward for 50 cm.")
bob.send("forward " + str(50), 10)
print ("Drone is going to turn counter-clockwise 135 degrees")
bob.send("ccw "+str(135), 5)

# Route B to E
for x in range(3):
    print ("Drone is moving forward for 80 cm.")
    bob.send("forward " + str(80), 10)
    print ("Drone is going to turn counter-clockwise 45 degrees")
    bob.send("ccw "+str(45), 5)

# Route E to F
print ("Drone is moving forward for 60 cm.")
bob.send("forward " + str(60), 10)
print ("Drone is going to turn counter-clockwise 45 degrees")
bob.send("ccw "+str(45), 5)

# Route F until A
print ("Drone is moving forward for 50 cm.")
bob.send("forward " + str(50), 10)

# A to origin angle
print ("Drone is going to turn clockwise 45 degrees")
bob.send("cw "+str(45), 5)

# ----------------------------------------

# Send the land command
bob.send("land ", 4)

# Print message
print ("Mission accomplished!")

# Close the socket
bob.sock.close()
