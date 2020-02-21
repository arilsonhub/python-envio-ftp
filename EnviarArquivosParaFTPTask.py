from FtpManager import FtpManager
import json

class EnviarArquivosParaFTPTask:

    def run(self):
        try:
            configData = self.getConfigData()
            self.sendFilesToFtpServer(configData)
            
        except Exception as e:
            print(e)

        

    def getConfigData(self):
        data = None
        try:
            with open('config.json') as jsonFile:
                data = json.load(jsonFile)

            if data is not None:
                return data
        except Exception as e:
            raise Exception("Não foi possível ler o arquivo de configuração")

    def sendFilesToFtpServer(self, configData):
        ftpConfig = configData['ftpConfig']
        ftpManager = FtpManager(ftpConfig['host'], ftpConfig['username'], ftpConfig['password'], ftpConfig['port'])
        ftpManager.sendFiles(configData)