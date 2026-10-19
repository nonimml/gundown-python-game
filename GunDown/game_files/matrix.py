#-------------------------------------------------------------------------------------------------------------
# matrix generator in cheat and normal mode
#-------------------------------------------------------------------------------------------------------------
def matrix_generation(no_rows ,no_column,mode,hidden_locations):
    if mode == True: #cheat mode enabled
        # Initialize counter
        counter = 1

        # Create the horizontal separator
        separator = "+---" * no_column + "+"

        # Generate and print the grid
        for r in range(no_rows):
            print(separator)  # Print separator before each row
            row_items = [] # Generate and print the grid
            for c in range(no_column): # Generate and print the grid
                if counter in hidden_locations: # Generate and print the grid
                    row_items.append("|  ")  # Hidden object location
                else:
                    row_items.append(f"|{counter:2}") 
                counter += 1                   #counter increment
            print(" ".join(row_items) + " |")  # Print the row
        print(separator)  # Final bottom border
        print() # Print a new line
    else:
        # Initialize counter
        counter = 1

        # Create the horizontal separator
        separator = "+---" * no_column + "+" #  Create the horizontal separator

        # Generate and print the grid
        for r in range(no_rows):
            print(separator)  # Print separator before each row
            row_items = [] 
            for c in range(no_column):
                row_items.append(f"|{counter:2}")
                counter += 1
            print(" ".join(row_items) + " |")
        print(separator)  # Final bottom border
        print() #   Print a new line
    return