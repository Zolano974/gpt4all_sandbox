#!/usr/bin/python3

# r
from langchain.llms import HuggingFaceHub
from langchain import PromptTemplate, LLMChain

import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

# prepare prompt
question = "Who won the FIFA World Cup in the year 1994? "

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

# choose model
repo_id = "tiiuae/falcon-40b"
#llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 64})

# prepare chain
#llm_chain = LLMChain(prompt=prompt, llm=llm)

#run chain
#print(llm_chain.run(question))


llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 64})
llm_chain = LLMChain(prompt=prompt, llm=llm)
print(llm_chain.run(question))




