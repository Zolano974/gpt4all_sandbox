#!/usr/bin/python3

from langchain.llms import GPT4All
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain import PromptTemplate, LLMChain

local_path = (
    "../models/GPT4All-13B-snoozy.ggmlv3.q4_0.bin"  # replace with your desired local file path
)


# Callbacks support token-wise streaming
callbacks = [StreamingStdOutCallbackHandler()]

# Verbose is required to pass to the callback manager
llm = GPT4All(model=local_path, callbacks=callbacks, verbose=True)

# If you want to use a custom model add the backend parameter
# Check https://docs.gpt4all.io/gpt4all_python.html for supported backends
llm = GPT4All(model=local_path, backend="gptj", callbacks=callbacks, verbose=True)


# prepare question
print("prepare question & context")
question = "Can you write me a complete Junit5 test class containing the unit tests for all the functions inmplemented in code given to you as context ?"

# Prepare context : content from the file
file_path = "../java/Toto.java"
#file_path = "../java/Toto2.java"

with open(file_path, 'r') as file:
    file_content = file.read().replace('\n', '')
context=file_content

#prompt
template = """
Please use the following context to answer questions.
Context: {context}
 - -
Question: {question}

Answer: Let's think step by step, one function at a time
"""

formatted_prompt = template.format(context=context, question=question)

print("prompt is ready")
print(formatted_prompt)

prompt = PromptTemplate(template=template, input_variables=["question", "context"])
# prompt

print("prepare chain")
llm_chain = LLMChain(prompt=prompt, llm=llm)


print("run chain")
llm_chain.run({
    "question": question,
    "context": context
})


# def download_model()
#     # from pathlib import Path
#     from tqdm import tqdm

#     Path(local_path).parent.mkdir(parents=True, exist_ok=True)

#     # Example model. Check https://github.com/nomic-ai/gpt4all for the latest models.
#     url = 'http://gpt4all.io/models/ggml-gpt4all-l13b-snoozy.bin'

#     # send a GET request to the URL to download the file. Stream since it's large
#     response = requests.get(url, stream=True)

#     # open the file in binary mode and write the contents of the response to it in chunks
#     # This is a large file, so be prepared to wait.
#     with open(local_path, 'wb') as f:
#         for chunk in tqdm(response.iter_content(chunk_size=8192)):
#             if chunk:
#                 f.write(chunk)