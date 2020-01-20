class SearchEngineBase(object):
    def __init__(self):
        pass

    def add_corpus(self, file_path):
        with open(file_path, "rb") as fin:
            text = fin.read().decode("utf-8")
        self.process_corpus(file_path, text)

    def process_corpus(self, _id, text):
        raise Exception("process_corpus not implemented")

    def search(self, query):
        raise Exception("search not implemented")


class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super(SimpleEngine, self).__init__()
        self.__id_to_texts = {}

    def process_corpus(self, _id, text):
        self.__id_to_texts[id] = text

    def search(self, query):
        results = []
        for _id, text in self.__id_to_texts.items():
            if query in text:
                results.append(_id)
        return results
