from gpt4all import GPT4All

# Initialize model
print("Initialize model")
model_name="nous-hermes-13b.ggmlv3.q4_0"
model_path = "../models/"
model = GPT4All(model_name, model_path)


# prepare question
print("prepare question & context")
question = "Can you write me a complete Junit5 test class containing the unit tests for the Java class given to you as context ? I want you to output complete test class, including at least 1 test method for each methods in the codeprovided as context"

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