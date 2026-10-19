# ----------------------------------------------------------------------------------------------------
# final matrix with found and missed objects
# ----------------------------------------------------------------------------------------------------
def check_found_missed(guess_positions, hidden_locations, no_rows, no_column):
    found_objects = list(set(guess_positions) & set(hidden_locations))
    missed_objects = list(set(hidden_locations) - set(guess_positions))
    # Initialize counter
    counter = 1  # Initialize counter

    # Create the horizontal separator
    separator = "+---" * no_column + "+"  # Create the horizontal separator

    # Generate and print the grid
    for r in range(no_rows):  # Generate and print the grid
        print(separator)  # Print separator before each row
        row_items = []
        for c in range(no_column):
            if counter in found_objects:
                row_items.append("| X")   # Found object
            elif counter in missed_objects:
                row_items.append("| H")   # Missed object
            else:
                row_items.append(f"|{counter:2}")  # Normal number
            counter += 1
        print(" ".join(row_items) + " |")
    print(separator)  # Final bottom border
    print()
    return found_objects, missed_objects
