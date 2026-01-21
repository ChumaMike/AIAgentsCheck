from langchain_ollama import ChatOllama

# 1. Initialize the Local Granite Model
# This connects to the Ollama app running in the background
llm = ChatOllama(
    model="granite3-dense:8b",
    temperature=0.1  # Low temperature for precise, "Architect" answers
)

# 2. The Test
print("🤖 Local Granite is warming up (running on your GPU/CPU)...")
response = llm.invoke("You are an IBM Hackathon winner. Suggest a 3-word slogan for an AI Governance tool.")

print("\n🔥 GRANITE SAYS:")
print(response.content)