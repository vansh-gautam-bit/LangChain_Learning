from langchain_google_genai import GoogleGenerativeAIEmbeddings
from setting import settings

embedding = GoogleGenerativeAIEmbeddings(model='gemini-embedding-001',dimensions=32,google_api_key=settings.GOOGLE_API_KEY)

documents=[
        "What is the meaning of life?",
        "What is the purpose of existence?"
        "How do I bake a cake?"
]

result = embedding.embed_documents(documents)

print(str(result))