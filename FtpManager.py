from ftplib import FTP 
import os
import fileinput

class FtpManager:

    def __init__(self,host,username,password,port):
        self.host = host
        self.username = username
        self.password = password
        self.port = port

    def getFtpConnectionInstance(self): 
        ftp = FTP()
        ftp.set_debuglevel(2)
        ftp.connect(self.host, self.port)
        ftp.login(self.username,self.password)

        return ftp

    def sendFiles(self, configData):
        ftpConnection = self.getFtpConnectionInstance()

        #ftp.cwd('/')

        pathToLocalFiles = configData['localConfig']['pathToFiles']
        localFileList = configData['localConfig']['fileList']

        for localFile in localFileList:
            localFilePath = pathToLocalFiles + "/" + localFile['pathToFile'] + "/" + localFile['fileName']
            pathToStoreInFtp = localFile['pathToStoreInFtp'] + "/" + localFile['fileName']
            isBinary = localFile['isBinary']

            filePointer = open(localFilePath, 'rb')

            if isBinary:
                ftpConnection.storbinary('STOR %s' % pathToStoreInFtp, filePointer, 1024)
            else:
                ftpConnection.storlines('STOR '+ pathToStoreInFtp, filePointer)
            
            filePointer.close()

        ftpConnection.quit()