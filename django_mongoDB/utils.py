from pymongo import MongoClient


def get_db_handle(username, password):
    # mongo connection string
    connection = 'mongodb+srv://{}:{}@cluster0.rthfj.mongodb.net/test?retryWrites=true&w=majority'.format(username,
                                                                                                          password)
    cluster = MongoClient(connection)

    # db name
    db = cluster["test"]

    # collection name
    collection = db['test']

    return collection
