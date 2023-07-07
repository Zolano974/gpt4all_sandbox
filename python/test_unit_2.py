from gpt4all import GPT4All

# Initialize model
print("Initialize model")
#model_name = "ggml-gpt4all-j-v1.3-groovy"
model_name="nous-hermes-13b.ggmlv3.q4_0"
model_path = "../models/"
model = GPT4All(model_name, model_path)


#prepare question & context
print("prepare question & context")
question = "Can you write me a Junit5 test class containing the unit tests for the code given to you as context ?"
q2 = "Can you tell me if this is nice code ?"

# Read the content from the file
file_path = "../java/Toto.java"
with open(file_path, 'r') as file:
    file_content = file.read().replace('\n', '')


#format prompt
template = """
Please use the following context to answer questions.
Context: {context}
 - -
Question: {question}
"""

formatted_template = template.format(context=file_content, question=question)

print("prompt is ready")
print(formatted_template)

print(".....")

for token in model.generate(formatted_template):
    print(token, end='', flush=True)

#prompt = PromptTemplate(template=template, input_variables=["context", "question"]).partial(context=file_path)




#print("running prompt")
# running prompt
#llm_chain = LLMChain(prompt=prompt, llm=gpt4all)
#response = llm_chain.run(question)
#print(response)