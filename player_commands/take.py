from commands.command import Command

class TakeCommand(Command):
    def __init__(self, info, description):
        Command.__init__(self, info, description)
        
    def execute(self, game, command):
        
        player = game.get_player()

        if command.get_command_length() > 1:
            if player.get_room().get_item(command.get_word(1)) is not None:
                #if player.get_value() + player.get_room().get_item(command.get_word(1)).get_value() <= player.get_value():
                if (player.get_room().get_item(command.get_word(1)).get_value() <= player.get_value()) & (player.get_room().get_item(command.get_word(1)).get_energy() >= -player.get_energy()):
                    player.pickup_item(player.get_room().get_item(command.get_word(1)))
                    player.set_value()
                    player.set_energy()
                    #player.get_room().remove_item(player.get_room().get_item(command.get_word(1)))
                    print("\nYou pick up the %s in the %s.\n" % (command.get_word(1), player.get_room().get_name().lower()))
                else:
                    if player.get_room().get_item(command.get_word(1)).get_value() >= player.get_value():
                      print("\n%s is much expensive!\n" % (player.get_room().get_item(command.get_word(1)).get_name()))
                    else:
                        
                          print("\nYou dont have enough energy for %s\n" % (player.get_room().get_item(command.get_word(1)).get_name()))
            else:
                print("\n%s not found in the %s.\n" % (command.get_word(1), player.get_room().get_name().lower()))
        else:
            print("\nTake what?\n")

    def usage(self):
        return "Usage: take [item]"
