from langchain_openrouter import ChatOpenRouter
from setting import settings, llm_cohere
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

chat_history=[
    SystemMessage(content='You are helpful AI assistant')
]

while True:
    user_input = input('You: ')
    # chat_history.append(user_input)
    chat_history.append(HumanMessage(content=user_input))

    if user_input == 'exit':
        break
     
    # result = llm_cohere.invoke(user_input)
    # result = llm_cohere.invoke(chat_history)
    result = llm_cohere.invoke(AIMessage(content=result.content))
    print("AI: ",result.content)

print(chat_history)