import random
# ----------------------------------------------------------------------------------------------------
# hidden object locations
# ----------------------------------------------------------------------------------------------------


def find_hidden_objects(hidden_count, cell_count):
    hidden_locations = []  # hidden are save in the list
    # randomly genarte the hidden locations and assign to the list
    hidden_locations = random.sample(range(1, cell_count), hidden_count)
    return hidden_locations  # return the hidden values
