from gevent.server import StreamServer
from mprpc import RPCServer
from spacy_api.api import *
from spacy_api.client import BaseClient
from spacy_api import api

class SpacyServer(RPCServer):

    def single(self, document, model, embeddings_path, attributes):
        return single(document, model, embeddings_path, attributes)

    def bulk(self, documents, model, embeddings_path, attributes):
        documents = tuple(documents)
        return bulk(documents, model, embeddings_path, attributes)

    def most_similar(self, word, n, model, embeddings_path):
        return most_similar(word, n, model, embeddings_path)


class SpacyLocalServer(BaseClient):

    api.get_nlp(model="C:/Users/Asus-Laptop/Desktop", embeddings_path="en_google")

    def single(self, document, attributes=None):
        return single(document, self.model, self.embeddings_path, attributes, local=True)

    def bulk(self, documents, attributes=None):
        documents = tuple(documents)
        return bulk(documents, self.model, self.embeddings_path, attributes, local=True)

    def most_similar(self, word, n):
        return most_similar(word, n, self.model, self.embeddings_path)


def serve(host="127.0.0.1", port=9033):
    print("Finish loading model")
    print("Serving spacy_api at {}:{}".format(host, port))
    server = StreamServer((host, int(port)), SpacyServer())
    server.serve_forever()
    #runs with command "spacy serve"


if __name__ == "__main__":
    serve()
