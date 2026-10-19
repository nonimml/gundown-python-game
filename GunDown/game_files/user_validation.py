import sys
# ----------------------------------------------------------------------------------------------------
# input_validation
# Description: This function validates the command line inputs for grid size and hidden object count.
# ----------------------------------------------------------------------------------------------------


def input_validation():
    help = None  # help variable
    mode = False  # mode variable
    banner = None  # banner variable
    # Display help information
    if len(sys.argv) == 2 and sys.argv[1].lower() == "help":
        print()
        help = open("game_files//help.txt", "r")  # open the help text file
        print(help.read())  # print the help information
        help.close()  # closing the help text file
        print()
        sys.exit()  # Exit the program after displaying help
    elif len(sys.argv) == 3:
        print()
        # open the game banner text file
        banner = open("game_files//game_banner.txt", "r")
        print(banner.read())  # print the game banner
        banner.close()  # closing the game banner text file
        print()
        return
    # enable the cheat mode
    elif len(sys.argv) == 4 and sys.argv[3].lower() == "show":
        mode = True  # set mode to True for cheat mode
        print()
        # open the game banner text file
        banner = open("game_files//game_banner.txt", "r")
        print(banner.read())  # print the game banner
        banner.close()  # closing the game banner text file
        print()
        return mode  # return mode for cheat mode
    else:
        # Invalid number of arguments
        print("Only two arguments allowed ex: gundown help or gundown 3x3 4")
        sys.exit()
    return


def grid_validation():
    try:
        grid_order = []  # list to store grid order
        # split the grid size input based on 'x'
        grid_order = sys.argv[1].split('x')
        # convert the first part to integer for rows
        no_rows = int(grid_order[0])
        # convert the second part to integer for columns
        no_column = int(grid_order[1])
        if no_rows >= 3 and no_column <= 5:
            return no_rows, no_column
        else:
            print("Invalid grid size !!! Rows should be >=3 and Columns should be <=5 ")
            sys.exit()
    except ValueError:  # exception handling for invalid input
        print("Invalid grid size format !!! Use Integers RowsxColumns (e.g., 3x4)")
        sys.exit()
    return


def hidden_obj_validation(no_rows, no_column):
    hidden_count = 0  # hidden count initialization
    try:
        # convert the hidden object count input to integer
        hidden_count = int(sys.argv[2])
        cell_count = no_rows * no_column  # calculate total cell count
        # validating hidden object count
        if 2 <= hidden_count <= round(cell_count/2) : # validate the hidden object count with the user input
            return hidden_count, cell_count  # return hidden object count and cell count
        else:
            print(f"Invalid hidden objects count !!! It should be  2 or {round(cell_count/2)}")
            sys.exit()
    except ValueError:  # exception handling for invalid input
        print("Invalid hidden objects count !!! It should be an Integer")
        sys.exit()
    return
