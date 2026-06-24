from langchain_openrouter import ChatOpenRouter
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint 
from setting import settings

llm_cohere = ChatOpenRouter(
    model='cohere/north-mini-code:free',
    api_key=settings.OPENROUTER_API_KEY)

llm_google = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    api_key=settings.GOOGLE_API_KEY
) 

# llm_qwen = HuggingFaceEndpoint(
#     repo_id='Qwen/Qwen3-0.6B',
#     task="text-generation",
#     huggingfacehub_api_token=settings.HUGGINGFACEHUB_ACCESS_TOKEN
# )

# model = ChatHuggingFace(llm=llm_qwen)

# result= model.invoke("what is the capital of india?")

result = llm_google.invoke("Are you not an ai model but you say you are an llm,explain?")

print(result.content)