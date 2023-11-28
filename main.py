class Singleton():

    def __int__(self, instance):
        self.instance = instance


    def Singleton(self):
        pass

    def getInstance(self):
        if self.instance == None:
            instance = Singleton()
        return instance

Clien = Singleton()


