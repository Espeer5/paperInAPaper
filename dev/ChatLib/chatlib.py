################################################################################
# chatlib.py                                                                   #
#                                                                              #
# :synopsis: This module provides a simple library for chatting with a chosen  #
# Llama model in a chatroom via Llama API. A chatroom is a space in the        #
# terminal where the user can make recurrent requests to the model and receive #
# responses back.                                                              #
#                                                                              #
# Author: Edward Speer                                                         #
# Revision Date: 10/21/24                                                      #
################################################################################

################################################################################
# IMPORTS                                                                      #
################################################################################

import json
import pickle as pkl
from typing import Dict, List, Tuple, IO

from openai import OpenAI

from ChatLib.config import *

################################################################################
# CLASS CHATCONTEXT                                                           #
################################################################################

"""
A chat context represents the state of a chatroom. It contains methods for 
sending requests to the model and handling responses. Responses are stored in
the file contained in the context's response_file attribute.
"""
class ChatContext:

    # ATTRIBUTES

    api:       OpenAI
    model:     str
    resp_file: str
    chat_log:  IO
    history:   List[Tuple[str, str]]

    # CONSTRUCTORS AND DESTRUCTORS

    def __init__(self, out_file):
        self.api       = OpenAI(api_key=API_KEY, base_url = API_URL)
        self.model     = MODEL
        self.resp_file = out_file
        self.chat_log  = open(self.resp_file, "w")
        self.history   = []
        self.chat_log.write(f"# CHAT LOG WITH MODEL {MODEL}\n\n")

    """
    ChatContext.destroy() -> None

    Releases all resources associated with the chat context.
    """
    def destroy(self) -> bool:
        self.chat_log.close()

    # METHODS

    """
    ChatContext.clear_history() -> None

    Clears the chat history for the particular session. This is useful for 
    sessions where each successive response is not dependent on the previous,
    as it will save significant token usage and therefore cost.
    """
    def clear_history(self) -> None:
        # Indicate history cleared in log and to stdout
        self.chat_log.write(
            "###_-_-_-_-_-_-_-_-_-_HISTORY CLEARED_-_-_-_-_-_-_-_-_-_\n")
        print("_-_-_-_-_-_-_-_-_-_HISTORY CLEARED_-_-_-_-_-_-_-_-_-_")
        self.history = []

    """
    ChatContext.load_history(history_file: str) -> None

    Loads a chat history (context) from a pickle file. This allows the
    conversation from a previous session to be continued in a new session later
    on. Note that these hisotries are not human readable.
    """
    def load_history(self, history_file: str) -> None:
        with open(history_file, "rb") as file:
            self.history = pkl.load(file)

    """
    ChatContext.save_history(history_file: str) -> None

    Saves the chat history (context) to a pickle file. This allows the
    conversation to be continued in a new session later on. Note that these
    histories are not human readable.
    """
    def save_history(self, history_file: str) -> None:
        with open(history_file, "wb") as file:
            pkl.dump(self.history, file)

    """
    ChatContext.send_request(request: str) -> Dict

    Sends a request to the model and returns the response JSON dict. The request
    will be sent with appropriate formatting out to the log file.
    """
    def send_request(self, request: str) -> Dict:
        # Add the user request to the chat history
        self.history.append(("user", request))
        
        # Form the api request based on the user message and the full message
        # history
        message_stream = [{"role": hist[0], "content": hist[1]} for hist in
                          self.history]
        response = self.api.chat.completions.create(
            model      = self.model,
            messages   = message_stream,
            max_tokens = MAX_TOKENS
        )

        # Write the request to the chat log
        self.chat_log.write(f"### USER:\n{request}\n")

        # Send the request to the model and return the response
        return json.loads(response.model_dump_json())

    """
    ChatContext.handle_response(response: Dict) -> None

    Handles the response from the model by both writing it to the chat log and
    printing it to the terminal. Not that the response may contain multiple 
    options for messages. This will be handled correctly here.
    """
    def handle_response(self, response: Dict) -> None:
        # For each message, write and print
        for message in response["choices"]:
            out_str = (f"### {MODEL}.{message['index']}:\n" +
                       f"{message['message']['content']}\n")

            # Write the message to the chat log
            self.chat_log.write(out_str)

            # Print the message to the terminal
            print(out_str)
        
        # If there are multiple responses, ask the user which one they prefer
        # to add to the chat history
        resp_num = 0
        if (len(response["choices"]) > 1):
            resp_num = int(input("Which response do you prefer? "))
        
        # Add the model response to the chat history
        self.history.append(("assistant",
                           response["choices"][resp_num]["message"]["content"]))
