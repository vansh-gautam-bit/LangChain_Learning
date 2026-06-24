from langchain_core.prompts import PromptTemplate
from langchain_openrouter import ChatOpenRouter
from setting import settings

llm_cohere = ChatOpenRouter(
    model='cohere/north-mini-code:free',
    api_key=settings.OPENROUTER_API_KEY)

model=llm_cohere

template2= PromptTemplate(
    template='Greet this person in 5 languages. the name of the person is {name}',
    input_variables=['name']
)
prompt= template2.invoke({'name':'nitish'})

result = model.invoke(prompt)

print(result.content)