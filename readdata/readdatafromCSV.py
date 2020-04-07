import pandas


class ReadData():

    def getCSVData(self):
        df = pandas.read_csv('F:/Miestro_PythonProject/credentials/portalCredentials.csv')
        return df


rd = ReadData()
value = rd.getCSVData()
