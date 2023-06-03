import utils
from utils import important_message

def main() -> None:

    """Передает полученную строку из stdin в функцию important_message()"""
    
    inp = input("Введите текст: ")
    print(important_message(inp))

# >>> main()
# Введите текст: The Python interpreter has a number of functions and types built into it that are always available. They are listed 
# here in alphabetical order.
# #===================================================================================================#
# #                                                                                                   #
# #  The Python interpreter has a number of functions and types built into it that are always availa  #
# #                          ble. They are listed here in alphabetical order.                         #
# #                                                                                                   #
# #===================================================================================================#

# >>> text = 'Return a Boolean value, i.e. one of True or False. x is converted using the standard truth testing
 # procedure. If x is false or omitted, this returns False; otherwise, it returns True. The bool class is a subclass of int (see Numeric
 # Types - int, float, complex). It cannot be subclassed further. Its only instances are False and True (see Boolean Values).'
# >>> msg = important_message(text)
# >>> print(msg)
# #===================================================================================================#
# #                                                                                                   #
# #  Return a Boolean value, i.e. one of True or False. x is converted using the standard truth test  #
# #  ing procedure. If x is false or omitted, this returns False; otherwise, it returns True. The bo  #
# #  ol class is a subclass of int (see Numeric Types - int, float, complex). It cannot be subclasse  #
# #               d further. Its only instances are False and True (see Boolean Values).              #
# #                                                                                                   #
# #===================================================================================================#