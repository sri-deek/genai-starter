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


# ### Embedding documents
documents = ["Hello world", "Goodbye world"]

# %%
# # embed_doc = embeddings.embed_documents(documents)
# with open('../data/embeddings/document_embeddings/embed_doc.pkl', 'wb') as f:
#     pickle.dump(embed_doc, f)
# embed_doc

# load document embeddings from file
with open('./data/embeddings/document_embeddings/embed_doc.pkl', 'rb') as f:
    embed_doc = pickle.load(f)
embed_doc

print(f"first document: {embed_doc[0]}")
print(f"second document: {embed_doc[1]}")
