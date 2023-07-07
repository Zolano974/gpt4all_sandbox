#!/usr/bin/python3

import os
import gpt4all

# Read the content from the file
file_path = "/home/zolano/Documents/GPT4ALL/java/Toto.java"
with open(file_path, 'r') as file:
    file_content = file.read().replace('\n', '')

# Initialize the model
model = gpt4all.GPT4All("ggml-gpt4all-j-v1.3-groovy")

# Add the file content as a system message to set the context
messages = [{"role": "system", "content": file_content}, 
            {"role": "user", "content": "This is the question prompt"}]

# Get the response from the model
response = model.chat_completion(messages)

# Print the response
print(response)