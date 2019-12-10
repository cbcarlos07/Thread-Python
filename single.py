from threading import Thread

class Th(Thread):

    def __init__ (self, num):
        Thread.__init__(self)
        self.num = num

    def run(self):

        print ("Thread ")
        t = Principal()
        t.testFn()


class Principal:

    a = Th(2)
    a.start()

    mensagem = 'Variavel da classe principal'

    def testFn(self):
        print ( self.mensagem )


