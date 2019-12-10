from threading import Thread

class Th(Thread):

    def __init__ (self, num):
        Thread.__init__(self)
        self.num = num

    def run(self):

        print ("Hello ")
        print (self.num)

        t = Teste()
        t.testFn()


class Teste:

    a = Th(2)
    a.start()

    def testFn(self):
        print ("teste funcao")


