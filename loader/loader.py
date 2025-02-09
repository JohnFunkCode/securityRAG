from database_access.docCrud import DocumentCRUD, DatabaseConnection
from database_access.engine_factory import EngineFactory
from grc_retriever import GRCRetriever
import logging

class Loader:
    def __init__(self):
        self.engine = EngineFactory().get_engine()
        self.doc_crud = DocumentCRUD(DatabaseConnection(self.engine))
        self.grc_retriever = GRCRetriever(self.doc_crud)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()
    logging.info("Starting loader...")
    loader = Loader()
    loader.grc_retriever.load_docs()
    logging.info("Loader finished")
