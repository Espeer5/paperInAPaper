################################################################################
# edit_cache.py                                                                #
#                                                                              #
# This module provides a simple library for editing the cached histories of    #
# the chatroom. It very simply allows the user to either print or load the     #
# cached history from the editing space in edit_space.py based on the command  #
# line arguments provided.                                                     #
#                                                                              #
# Author: Edward Speer                                                         #
# Revision Date: 10/24/24                                                      #
################################################################################

################################################################################
# IMPORTS                                                                      #
################################################################################

import pickle as pkl
import sys

# If we are saving a previously edited history, we load it from the edit_space
if (sys.argv[1] == "save"):
    from edit_space import HISTORY
    

################################################################################
# CONSTANTS                                                                    #
################################################################################

# Path to cache file container directory
CACHE_PATH = "../"

# Default conversation cache to store long-term conversation history
CACHE_FILE = CACHE_PATH + "conversation_cache.pkl"

# path to the edit_space file
EDIT_SPACE = "edit_space.py"

################################################################################
# MAIN                                                                         #
################################################################################

"""
main() -> None

USAGE: python edit_cache.py [command] [cache_file]

Main function for the edit_cache module. Handles command line arguments to 
either print a cached history out the edit_space to be edited, or load a
previously edited history back into the cache.
"""
def main() -> None:
    if (sys.argv[1] == "edit"):
        if (len(sys.argv) == 2):
            with open(CACHE_FILE, 'rb') as f:
                history = pkl.load(f)
        else:
            with open(sys.argv[2], 'rb') as f:
                history = pkl.load(f)
        with open(EDIT_SPACE, 'a') as editor:
            editor.write(f"{history}")
    elif (sys.argv[1] == "save"):
        if (len(sys.argv) == 2):
            with open(CACHE_FILE, 'wb') as f:
                pkl.dump(HISTORY, f)
        else:
            with open(sys.argv[2], 'wb') as f:
                pkl.dump(HISTORY, f)
        

if __name__ == "__main__":
    main()
