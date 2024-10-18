################################################################################
# chatlib.py                                                                   #
#                                                                              #
# :synopsis: This module provides a simple library for chatting with a chosen  #
# Llama model in a chatroom via Llama API. A chatroom is a space in the        #
# terminal where the user can make recurrent requests to the model and receive #
# responses back.                                                              #
#                                                                              #
# Author: Edward Speer                                                         #
# Revision Date: 10/17/24                                                      #
################################################################################

################################################################################
# IMPORTS                                                                      #
################################################################################

import json
import typing

from llamaapi import LlamaAPI

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

    api:       LlamaAPI
    model:     str
    resp_file: str
    chat_log:  typing.IO

    # CONSTRUCTORS AND DESTRUCTORS

    def __init__(self, out_file):
        self.api       = LlamaAPI(API_KEY)
        self.model     = MODEL
        self.resp_file = out_file
        self.chat_log  = open(self.resp_file, "w")
        self.chat_log.write(f"# CHAT LOG WITH MODEL {MODEL}\n\n")

    """
    ChatContext.destroy() -> None

    Releases all resources associated with the chat context.
    """
    def destroy(self) -> bool:
        self.chat_log.close()

    # METHODS

    """
    ChatContext.send_request(request: str) -> Dict

    Sends a request to the model and returns the response JSON dict. The request
    will be sent with appropriate formatting out to the log file.
    """
    def send_request(self, request: str) -> typing.Dict:
        # Form the api request based on the user message
        api_request = {
            "messages": [{"role": "user", "content": request}],
            "stream":   False,
            "max_tokens": 500,
        }

        # Write the request to the chat log
        self.chat_log.write(f"### USER:\n{request}\n")

        # Send the request to the model and return the response
        return json.loads(json.dumps(self.api.run(api_request).json()))

    """
    ChatContext.handle_response(response: Dict) -> None

    Handles the response from the model by both writing it to the chat log and
    printing it to the terminal. Not that the response may contain multiple 
    options for messages. This will be handled correctly here.
    """
    def handle_response(self, response: typing.Dict) -> None:
        # For each message, write and print
        for message in response["choices"]:
            out_str = (f"### {MODEL}.{message['index']}:\n" +
                       f"{message['message']['content']}\n")

            # Write the message to the chat log
            self.chat_log.write(out_str)

            # Print the message to the terminal
            print(out_str)
