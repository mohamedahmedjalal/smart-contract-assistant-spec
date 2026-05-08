from langchain_groq import ChatGroq
from langchain_classic.chains import ConversationalRetrievalChain

from app.config import MODEL_NAME
from app.embeddings import load_vectorstore
from app.memory import memory

vectorstore = load_vectorstore()
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

llm = ChatGroq(
    temperature=0, 
    groq_api_key="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", 
    model_name="meta-llama/llama-4-scout-17b-16e-instruct"
)

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory,
    return_source_documents=True,
)


def ask_question(question):
    response = qa_chain.invoke({"question": question})

    answer = response["answer"]
    docs = response["source_documents"]

    citations = "\n\nSources:\n"

    for i, doc in enumerate(docs):
        citations += f"[{i+1}] {doc.page_content[:250]}...\n"

    return answer + citations
