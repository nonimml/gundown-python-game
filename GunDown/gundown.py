import sys
import random
import datetime
from game_files  import matrix 
from game_files import user_validation
from game_files import hidden_obj_placement
from game_files import final_matrix
#----------------------------------------------------------------------------------------------------
#final results
#----------------------------------------------------------------------------------------------------
def final_results(hidden_locations,found_objects):
   print("Final Results")
   print("Hidden locations : ", *hidden_locations,sep=',')#unpack and add a comma in between the values      
   print("Found  locations : ", *found_objects,sep=',')#unpack and add a comma in between the values
   print(f"{len(found_objects)}  of  {len(hidden_locations)} found ({len(found_objects)/len(hidden_locations)*100:.0f}%)")
   now = datetime.datetime.now()                 # Get the current local date and time from the system clock 
   date_str = now.strftime("%Y%m%d")             # Get the current local date from the system clock separately
   time_str = now.strftime("%H%M")               # Get the current local time from the system clock separately
   random_code = random.randint(1000, 9999)      # creating a random 4 digit number for the text file name
   if mode == True:
      filename = str(str(date_str) + "_" + str(time_str) + "_" + str(random_code) + "C.txt")  # if it is normal mode then just the filename with "C"
   else:
      filename = str(str(date_str) + "_" + str(time_str) + "_" + str(random_code) + ".txt")  # if it is normal mode then just the filename without "C"
   fo=None
   fo=open(filename, "w")                     # open the file in write mode
   fo.write("Date : " + str(now.strftime("%Y-%m-%d")))  # writing the current date in the text file
   fo.write("\n")# writing a new line in the text file
   fo.write("Time : " + str(now.strftime("%H:%M")))  # writing the current time in the text file
   fo.write("\n")# writing a new line in the text file
   fo.write("Hidden locations : "+ str(hidden_locations ))
   fo.write("\n")# writing a new line in the text file
   fo.write("Found objects    : "+ str(found_objects ))
   fo.write("\n")# writing a new line in the text file
   fo.write(f"{len(found_objects)}  of  {len(hidden_locations)} found ({len(found_objects)/len(hidden_locations)*100:.0f}%)")  # writing the summary in the text file
   fo.close()# closing the text file
   print()
   end=None #end game banner variable
   end=open("game_files//end_game_banner.txt","r")# open the end game banner text file
   print(end.read())# print the end game banner
   end.close()# closing the end game banner text file
   return
    
#---------------------------------------------------------------------------------------------------------------------
# Main flow
#---------------------------------------------------------------------------------------------------------------------
mode=user_validation.input_validation()                                                                 #get the mode (cheat/normal)
no_rows ,no_column=user_validation.grid_validation()                                                    #get the grid size
hidden_count,cell_count=user_validation.hidden_obj_validation(no_rows ,no_column)                       #get the hidden object count and cell count
hidden_locations=hidden_obj_placement.find_hidden_objects(hidden_count,cell_count)                      #get hidden object locations
matrix.matrix_generation(no_rows, no_column,mode,hidden_locations)                                      #generate the matrix based on mode
guess_positions=hidden_obj_placement.hidden_object_placement(hidden_count,no_rows,no_column)            #get user guessed positions
found_objects, missed_objects=final_matrix.check_found_missed(guess_positions, hidden_locations, no_rows, no_column)  #generate the final matrix with found and missed objects
final_results(hidden_locations,found_objects)                                                                         #display final results

