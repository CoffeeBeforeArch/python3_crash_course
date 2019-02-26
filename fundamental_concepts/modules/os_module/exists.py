# This program uses the "os" module to verify that a file exists
# By: Nick from CoffeeBeforeArch

from sys import argv

# Import exists to check file existence
from os.path import exists

# Get program name and file path from command line
program_name, path_to_file = argv

# Check to see the existence of a file
print(exists(path_to_file))
