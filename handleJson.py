import json, os


class HandleJson:
    
    def __init__(self, path: str):
        self.path = path
        self.data = []
            
    def extract(self):
        if os.path.exists(self.path):
            with open(self.path, mode='r', encoding='utf-8') as json_datoteka:
                self.data = json.load(json_datoteka)
                json_datoteka.close()
        return self.data

    def append(self, data):
        self.data = self.extract()
        with open(self.path, mode='w', encoding='utf-8') as json_datoteka:
                self.data.append(data)
                json.dump(self.data, json_datoteka)
                json_datoteka.close()