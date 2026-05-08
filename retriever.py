from app.embeddings import load_vectorstore

vectorstore = load_vectorstore()


def retrieve_documents(query, k=4):
    retriever = vectorstore.as_retriever(search_kwargs={"k": k})
    return retriever.get_relevant_documents(query)
