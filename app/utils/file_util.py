import json


class FileUtil:
    _config = None

    @staticmethod
    def getConfig():
        if not FileUtil._config:
            with open('config.json', 'r') as file:
                FileUtil._config = json.loads(file.read())
            return FileUtil._config
        else:
            return FileUtil._config