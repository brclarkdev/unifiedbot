import os
import chainlit as cl
from langchain import HuggingFaceHub, PromptTemplate, LLMChain


model_id = 'tiiuae/falcon-7b-instruct'

falcon_llm = HuggingFaceHub(huggingfacehub_api_token=os.environ['HF_API_KEY'], repo_id=model_id,model_kwargs={"temperature":0.8,"max_new_tokens":2000})

template = """

You are an sarcastic AI assistant that provides answers to user queries.

{message}

"""
prompt = PromptTemplate(template=template, input_variables=['message'])

falcon_chain = LLMChain(llm=falcon_llm,prompt=prompt,verbose=True)

@cl.on_chat_start
async def on_chat_start():
    elements = [cl.Image(name="image1", display="inline", path="./good_day.jpg")]
    await cl.Message(content="Hello there, Welcome to AskAnyQuery related to Data!", elements=elements).send()

@cl.on_message
async def main(message: str):

    # Get data
    df = cl.user_session.get('data')

    # Agent creation
    #agent = create_agent(df, llm)

    # Run model 
    #response = agent.run(message)

    # Send a response back to the user
    await cl.Message(content="hello world",).send()
# @cl.on_message
# async def main(message: str):
#     # Your custom logic goes here...
#     prompt = PromptTemplate(template=template, input_variables=['message'])

#     falcon_chain = LLMChain(llm=falcon_llm,prompt=prompt,verbose=True)
#     # Send a response back to the user
#     await cl.Message(
#         content=f"Received: {falcon_chain}",
#     ).send()

# print(falcon_chain.run("What are the colors in the Rainbow?"))

# @cl.langchain_factory(use_async=False)
# def factory():

#     prompt = PromptTemplate(template=template, input_variables=['question'])
#     falcon_chain = LLMChain(llm=falcon_llm,prompt=prompt, verbose=True)
#     return falcon_chain
