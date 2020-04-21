import json


class ReadDataFromJSON():
    f = open('F:/Miestro_PythonProject/credentials/MiestroCredentials.json')

    # Iterating through the json list
    def getValueFromJSON(self):
        # Opening JSON file

        # Returns JSON object as a Dictionary
        data = json.load(self.f)

        for i in data['Credentials']:
            value = i
        return value


rd = ReadDataFromJSON()
value1 = rd.getValueFromJSON()

rd.f.close()
