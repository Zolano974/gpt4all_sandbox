# GPT 4 ALL LOCALLY

Micro Sandbox project to play with GPT4ALL locally on linux

## install gpt4all Linux

Pre-requisites : 

- python3.7+ 
- pip
- git

```bash
git clone https://github.com/nomic-ai/gpt4all.git

#gpt4all standalone
pip install gpt4all typer 

#langchain
pip install langchain pyllamacpp
pip install huggingface_hub transformers datasets
```

Download 1 or more models : (complete list here : https://gpt4all.io/index.html ) 

Put them in models/ dir

Tested with nous-hermes-13b.ggmlv3.q4_0.bin

## Launch CLI
```bash
cd gpt4all/gpt4all-bindings/cli
python app.py repl
```

## Python Scripts

```bash
cd python
python3 test_unit_2.py
```

Doc: 
https://nomic-ai.github.io/pygpt4all/

## Hugging face
Doc here : https://python.langchain.com/docs/ecosystem/integrations/huggingface
and here : https://python.langchain.com/docs/modules/model_io/models/llms/integrations/huggingface_hub.html

- Create huggingface account

```
pip install huggingface_hub
export HUGGINGFACEHUB_API_TOKEN=`my_hf_token`
```
export HUGGINGFACEHUB_API_TOKEN=`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`
