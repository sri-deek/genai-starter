### Import libraries
# inbuit
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_openai import OpenAIEmbeddings
import os
import pickle

# user defined
from config import set_environment



# ### Set environment variables
set_environment()

# os.environ['GOOGLE_API_KEY']


# ### Create an instance of the GoogleGenerativeAIEmbeddings class


embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")


# ### use embeddings to embed text and save in file



# first_embed = embeddings.embed_query("What is the capital of France?")
# type(first_embed)
# with open('../data/embeddings/text_embeddings/first_embed.pkl', 'wb') as f:
#     pickle.dump(first_embed, f)
# first_embed



# ### load text embeddings from file

with open('./data/embeddings/text_embeddings/first_embed.pkl', 'rb') as f:
    first_embed = pickle.load(f)
first_embed

print(type(first_embed))
print(len(first_embed))
print(first_embed[:5])  # Print the first 5 elements of the embedding vector