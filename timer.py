"""
This program is used for MGTC28 Nerve of Steel Game.
timer.py is a simple Python script that will allow user to set timer duration.
Upon timer expiry, user will see the time up meme and sound notification.
timer.py uses the time library to help keep track of time
"""


# This program is timer that counts down


import time # The time library has a sleep function that will pause the script for a specifized amount of time
import random 

print ("Players Stand")


# Sleep for a random time between 5 to 25 seconds
set_time = random.randint(5, 25)

time.sleep(set_time)

# When sleep is over
print("Time Up. Last to sit down wins.")
