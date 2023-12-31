from gpt4all import GPT4All

# Initialize model
print("Initialize model")
model_name="nous-hermes-13b.ggmlv3.q4_0"
model_path = "../models/"
model = GPT4All(model_name, model_path)


# prepare question
print("prepare question & context")
question = "Can you write me a complete Junit5 test class containing the unit tests for all the functions inmplemented in code given to you as context ?"
q2 = "Can you tell me if this is nice code ?"

# Prepare context : content from the file
file_path = "../java/Toto.java"
#file_path = "../java/Toto2.java"

with open(file_path, 'r') as file:
    file_content = file.read().replace('\n', '')

#format prompt
template = """
Please use the following context to answer questions.
Context: {context}
 - -
Question: {question}
"""

formatted_prompt = template.format(context=file_content, question=question)

print("prompt is ready")
print(formatted_prompt)

print(">asking model...")

for token in model.generate(
    formatted_prompt,
    temp=0.3
):
    print(token, end='', flush=True)