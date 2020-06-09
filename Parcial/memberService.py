from repository import Repository


class MemberService():

    def __init__(self):
        pass

    def add_member(self, member):
        lKey = -1
        for key in Repository.membersList:
            lKey = key
        lKey = lKey + 1
        Repository.membersList[lKey] = member.__dict__
        return lKey

    def update_member(self, legajo, member):
        lastKey = len(Repository.membersList)
        if legajo > lastKey:
            raise ValueError
        Repository.membersList[legajo]['_name'] = member._name
        Repository.membersList[legajo]['_surname'] = member._surname
        Repository.membersList[legajo]['_age'] = member._age
        Repository.membersList[legajo]['_phone'] = member._phone

    def delete_member(self, legajo):
        lastKey = len(Repository.membersList)
        if legajo > lastKey:
            raise ValueError
        del Repository.membersList[legajo]
