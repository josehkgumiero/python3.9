################################################################

#import os

# get the current working directory
#current_working_directory = os.getcwd()

# print output to the console
#print(current_working_directory)


################################################################

# pwd

################################################################

import os
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))

################################################################