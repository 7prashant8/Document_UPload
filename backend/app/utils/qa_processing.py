from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex

INDEX_DIR = "index/"

def answer_question(pdf_path: str, question: str) -> str:
    # Load or build the index
    if not os.path.exists(INDEX_DIR):
        os.makedirs(INDEX_DIR)
    index_path = f"{INDEX_DIR}{pdf_path.split('/')[-1]}.json"
    
    if os.path.exists(index_path):
        index = GPTSimpleVectorIndex.load_from_disk(index_path)
    else:
        documents = SimpleDirectoryReader(pdf_path).load_data()
        index = GPTSimpleVectorIndex.from_documents(documents)
        index.save_to_disk(index_path)
    
    # Query the index
    response = index.query(question)
    return response.response
