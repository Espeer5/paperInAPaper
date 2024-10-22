################################################################################
# run_chat.py                                                                  #
#                                                                              #
# This script runs a chatroom using ChatLib in accordance with the user's      #
# ChatLib config. The file name of the chat log is assigned automatically.     #
#                                                                              #
# Author: Edward Speer                                                         #
# Revision Date: 10/21/24                                                      #
################################################################################

################################################################################
# IMPORTS                                                                      #
################################################################################

from datetime import datetime
from pathlib import Path

from ChatLib.chatlib import ChatContext
from ChatLib.config import MODEL

################################################################################
# CONSTANTS                                                                    #
################################################################################

# Path to log file container directory
LOG_PATH = "../logs/chats/"


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

    while True:
        user_input = input("You: ")
        if user_input == "exit":
            break
        elif user_input == "clear":
            chat.clear_history()
        else:
            response = chat.send_request(user_input)
            chat.handle_response(response)


if __name__ == "__main__":
    main()
