class ResponseModel:
    data = None
    count = None

    def __init__(self, data):
        if isinstance(data, list):
            self.count = len(data)
        self.data = data

    @staticmethod
    def __attrs():
        attrs = ['data', 'count']
        return attrs[:]

    def toJSON(self):
        attrs = ResponseModel.__attrs()
        json = {}
        for k in attrs:
            json[k] = self.__dict__.get(k)
        return json