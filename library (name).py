# example 1
from colorama import Fore 
import pyfiglet

font1 = pyfiglet.figlet_format('Insha Habib', justify='center', width=140)
# font2 = pyfiglet.figlet_format('Muhammad Sharjeel Saleem', justify='center', width=140)
print(Fore.YELLOW + font1)
# print(Fore.YELLOW + font2)

# example 2
import pyfiglet
from termcolor import colored

def name():
    message=pyfiglet.figlet_format('Insha Habib', justify='center', width=140)
    colored_msg=colored(message, color='blue')
    print(colored_msg)

name()

