import os
from datetime import datetime
fullpath=os.path.abspath
class Logger:
    def __init__(self) -> None:
        """         with open('./proyecto/log/log.txt','a+') as file:
                    self.file=file """
        if not os.path.exists('./proyecto/log'):
            os.makedirs('./proyecto/log')
        self.file=open('./proyecto/log/log.txt','a+')
    
    def message(self,msg:str):
        hour=datetime.now()
        hour_str=str(hour)
        self.file.write(hour_str+'|'+msg+'\n')
    
    def showLog(self):
        self.file.seek(0)
        print("Bitácora de acciones realizadas:")
        print(self.file.read())
        
    def close(self):
        self.file.close()