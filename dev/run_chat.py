################################################################################
# run_chat.py                                                                  #
#                                                                              #
# This script runs a chatroom using ChatLib in accordance with the user's      #
# ChatLib config. The file name of the chat log is assigned automatically.     #
#                                                                              #
# Author: Edward Speer                                                         #
# Revision Date: 10/21/24                                                      #
################################################################################

"""
USAGE: python run_chat.py [cache_file]

cache_file: the name of the cache file to load, or "default" for the 
            default cache file

Options on user prompt:
- "exit"              exit the chatroom
- "clear"             clear the chat history
- "save [cache_file]" save the chat history to cache. If no cache file is
                      specified, the default cache file is used.
- "load [cache_file]" load the chat history from cache. If no cache file is
                      specified, the default cache file is used.
"""

################################################################################
# IMPORTS                                                                      #
################################################################################

from datetime import datetime
from pathlib import Path
import sys

from ChatLib.chatlib import ChatContext
from ChatLib.config import MODEL

################################################################################
# CONSTANTS                                                                    #
################################################################################

# Path to log file container directory
LOG_PATH = "../logs/chats/"

# Path to cache file container directory
CACHE_PATH = "../cache/"

# Default conversation cache to store long-term conversation history
CACHE_FILE = CACHE_PATH + "conversation_cache.pkl"

################################################################################
# HELPER FUNCTIONS                                                             #
################################################################################

"""
auto_log_name() -> str

Auto-generates a chat log file name based on the current date and time. Offers
the user the ability to append a custom suffix to the file name.
"""
def auto_log_name() -> str:
    now       = datetime.now()
    date      = now.strftime("%m-%d-%Y/")
    time      = now.strftime("%H-%M-%S")
    suffix    = input("Enter a custom suffix for the chat log file" + 
                      "(leave blank for none): ")

    # Ensure the parent directory for the logfile exists
    Path(LOG_PATH + date).mkdir(parents=True, exist_ok=True)

    return f"{LOG_PATH}{date}log_{time}_{suffix}.md"

################################################################################
# MAIN                                                                         #
################################################################################

def main() -> None:
    chat = ChatContext(auto_log_name())

    print("LOG OUTPUT FILE AT PATH: " + chat.resp_file)

    # First command line argument specifies cache file to load. If "default",
    # the default cache file is loaded. If none, no cache file is loaded.
    if len(sys.argv) > 1:
        if sys.argv[1] == "default":
            chat.load_history(CACHE_FILE)
        
        else:
            chat.load_history(CACHE_PATH + sys.argv[1])

    while True:
        user_input = input("You: ")
        if user_input == "exit":
            break
        elif user_input == "clear":
            chat.clear_history()
        elif user_input.startswith("load"):
            if len(user_input.split()) == 1:
                chat.load_history(CACHE_FILE)
            else:
                chat.load_history(CACHE_PATH + user_input.split()[1])
        elif user_input.startswith("save"):
            if len(user_input.split()) == 1:
                chat.save_history(CACHE_FILE)
            else:
                chat.save_history(CACHE_PATH + user_input.split()[1])
        else:
            response = chat.send_request(user_input)
            chat.handle_response(response)


if __name__ == "__main__":
    main()
