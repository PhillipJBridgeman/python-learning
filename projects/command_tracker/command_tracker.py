"""
Command Tracker
"""
# This script will track the commands entered by user and output them in a ordered dictionary.
# It will also allow the user to view the commands in a specific order.
from collections import OrderedDict

command_history = OrderedDict()

while True:
    command = input("Enter a command (or 'exit' to quit): ")
    if command.lower() == 'exit' or command.lower() == 'quit':
        break
    if command in command_history:
        del command_history[command]
    command_history[command] = None

print("\nCommand History:")
for cmd in command_history.keys():
    print(cmd)
