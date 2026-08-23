from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader, WebBaseLoader

def load_directory(path: str):
    pdf_loader = DirectoryLoader(path, glob="**/*.pdf", loader_cls=PyPDFLoader)
    text_loader = DirectoryLoader(path, glob="**/*.txt", loader_cls=TextLoader)
    return pdf_loader.load() + text_loader.load()

def load_web(url: str):
    return WebBaseLoader(url).load()
if __name__ == "__main__":
    docs = load_directory("./data")
    print(docs[0].page_content)