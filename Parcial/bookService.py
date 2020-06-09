from repository import Repository


class BookService():

    def __init__(self):
        pass

    def add_book(self, book):
        lKey = -1
        for key in Repository.booksList:
            lKey = key
        lKey = lKey + 1
        Repository.booksList[lKey] = book.__dict__
        return lKey

    def update_book(self, key, update):
        lastKey = len(Repository.booksList)
        if key > lastKey:
            raise ValueError
        Repository.booksList[key]['_name'] = update._name
        Repository.booksList[key]['_authorName'] = update._authorName

    def assign_book(self, id, legajo):
        condicion = len(Repository.booksList)
        if condicion < id:
            raise ValueError
        condicion2 = len(Repository.membersList)
        if condicion2 < legajo:
            raise ValueError
        Repository.booksList[id]['_memberLegajo'] = legajo
