from colorama import init, Fore, Back, Style


def colourful_print(type, str):
    init(wrap=True, autoreset=True)

    if type.upper() == 'PRIMARY':
        print(Fore.WHITE + Back.BLUE + Style.BRIGHT + str)
    elif type.upper() == 'SUCCESS':
        print(Fore.WHITE + Back.GREEN + Style.BRIGHT + str)
    elif type.upper() == 'WARNING':
        print(Fore.WHITE + Back.YELLOW + Style.BRIGHT + str)
    elif type.upper() == 'ERROR':
        print(Fore.WHITE + Back.RED + Style.BRIGHT + str)
    else:
        print(str)
