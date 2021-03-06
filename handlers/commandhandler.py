from player_commands.go import GoCommand
from player_commands.look import LookCommand
from player_commands.inform import InformCommand
from player_commands.items import ItemsCommand
from player_commands.take import TakeCommand
from player_commands.help import HelpCommand
from player_commands.quit import QuitCommand



class CommandHandler:
    def __init__(self):
        self.commands = {}
        self.load_player_commands()
    
    def load_player_commands(self):
        self.commands["go"] = GoCommand("go [direction]", "Choose a direction to go.")
        self.commands["look"] = LookCommand("look", "Look around the room you are currently in.")
        self.commands["inform"] = InformCommand("information", "Informations about items and characters in the current room.")
        self.commands["items"] = ItemsCommand("items", "View the items in the player house.")
        self.commands["take"] = TakeCommand("take [item]", "Pick up an item from the room you are currently in.")
        self.commands["help"] = HelpCommand("help", "Access the help menu.")
        self.commands["quit"] = QuitCommand("quit", "Quit the game.")
    
    def get_commands_list(self):
        return self.commands

    def add_command(self, command):
        self.commands.add(command.get_name(), command)
    
    def get_command(self, command_word):
        return self.commands.get(command_word)
        
        
    