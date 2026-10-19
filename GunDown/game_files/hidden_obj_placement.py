import random #importing random module
#----------------------------------------------------------------------------------------------------
# hidden object locations
#----------------------------------------------------------------------------------------------------
def find_hidden_objects(hidden_count,cell_count):                       #hidden object locations
  hidden_locations =[]                                                  #list to store hidden object locations
  hidden_locations= random.sample(range(1,cell_count),hidden_count)     #generate unique random positions for hidden objects
  return hidden_locations                                               #return the list of hidden object locations
#-------------------------------------------------------------------------------------------------------
# hidden object placement
#-------------------------------------------------------------------------------------------------------
def hidden_object_placement(hidden_count,no_rows,no_column):                                      #hidden object placement
    guess_positions =[]                                                                           #list to store user guessed positions
    temp_position =0                                                                              #temporary variable to hold user input
    guess_count=0                                                                                 #counter for number of guesses
    while guess_count < hidden_count:                                                             #loop until user has guessed all hidden objects
      guess_count +=1                                                                             #increment guess counter
      try:                                                                                        #exception handling for invalid input
          temp_position = int(input(f"Guess hidden object location {guess_count} of {hidden_count} : "))#get user input
          if temp_position not in guess_positions and 1 <= temp_position <= no_rows * no_column:        #check for duplicate and valid range
             guess_positions.append(temp_position)                                                      #add valid position to list
          else:
              print("Duplicate position entered or value is not in the column range !!! Please enter a different position")
              guess_count -=1
      except :
          print("Invalid input !!! Please enter an Integer value for position")                         #exception message
          temp_position = int(input(f"Guess hidden object location {guess_count} of {hidden_count} : "))#get user input
    print()
    return guess_positions                                                                              #return the list of guessed positions