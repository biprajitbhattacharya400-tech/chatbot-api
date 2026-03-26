# import os
# from groq import Groq
# from dotenv import load_dotenv


# from sentence_transformers import SentenceTransformer

# model = SentenceTransformer('all-MiniLM-L6-v2')
# pip install -U langchain langchain-core langsmith langgraph
# embedding = model.encode("Hello world")

# print(embedding)



# documents = [
#     "FastAPI is a modern Python web framework used for building APIs quickly and efficiently.",
    
#     "SQLAlchemy is an ORM (Object Relational Mapper) that allows interaction with databases using Python code.",
    
#     "RAG stands for Retrieval Augmented Generation, a technique that improves AI responses by providing external context.",
    
#     "Large Language Models (LLMs) generate human-like text but may not always have updated or domain-specific knowledge.",
    
#     "Python is widely used for backend development, machine learning, and AI applications.",
    
#     "In RAG systems, documents are searched first and then passed to the LLM to generate accurate answers.",
# ]



# def search_docs(query):
#     results = []
#     query_words = query.lower().split()

#     for doc in documents:
#         score = 0

#         for word in query_words:
#             if word in doc.lower():
#                 score += 1

#         if score > 0:
#             results.append((score, doc))

#     # Sort by relevance (highest score first)
#     results.sort(reverse=True)

#     # Return top 3 documents
#     return [doc for score, doc in results[:3]]




# load_dotenv()
# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "What is FastAPI",
#         }
#     ],
#     model="llama-3.3-70b-versatile",
# )

# print(chat_completion.choices[0].message.content)