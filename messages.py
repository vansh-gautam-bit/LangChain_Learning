from langchain.messages import SystemMessage , HumanMessage , AIMessage
from setting import settings, llm_cohere

messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

result = llm_cohere.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)

