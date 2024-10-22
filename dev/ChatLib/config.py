################################################################################
# config.py                                                                    #
#                                                                              #
# This file defines the configurable settings for the chatlib module.          #
#                                                                              #
# Author: Edward Speer                                                         #
# Revision Date: 10/17/24                                                      #
################################################################################

# Base URL for accessing the Llama API
API_URL = "https://api.llama-api.com"

# Personal API key for accessing the Llama API
with open("/Users/espeer/secrets.txt") as api_key_file:
    API_KEY = api_key_file.read().strip()

# The model to chat with
MODEL = "llama3.1-70b"
