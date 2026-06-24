from langchain_openrouter import ChatOpenRouter
from setting import settings, llm_cohere

chat_history=[]

while True:
    user_input = input('You: ')
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    # result = llm_cohere.invoke(user_input)
    result = llm_cohere.invoke(chat_history)
    print("AI: ",result.content)

print(chat_history)