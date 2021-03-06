#!/bin/python3
import commands
import sys
from userInterface import Option

def option_choice_is_valid(choice,options):
    return choice in options or choice.upper() in options

def get_option_choice(options):
    try:
        choice = input("Choose an option: ")
    except:
        print("\vGood bye!")
        sys.exit()
        
    while not option_choice_is_valid(choice,options):
        print('Invalid choice')
        choice=input("Choose an option: ")
    return options[choice.upper()]

def print_options(options):
    for shortcut, option in options.items():
        print(f'({shortcut}){option}')
    print()
    
if __name__ == "__main__":
    commands.CreateBookmarksTableCommand().execute()

    options = {
            'A':Option('Add a bookmark',commands.AddBookmarkCommand()),
            'B':Option('List bookmarks by date',commands.ListBookmarksCommand()),
            'T':Option('List bookmarks by title',commands.ListBookmarksCommand(order_by='title')),
            'D': Option('Delete a bookmark', commands.DeleteBookmarkCommand()),
            'Q': Option('Quit',commands.QuitCommand()),
            }
    print_options(options)
    chosen_option = get_option_choice(options)
    chosen_option.choose()
