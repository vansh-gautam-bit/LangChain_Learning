
from setting import llm_cohere , settings

model = llm_cohere

result = model.invoke("Hello how are you , and how can you help me ?")

print(result.content)

