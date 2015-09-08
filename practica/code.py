__author__ = 'Manuel'


class Clase(object):
    name = ""
    dni = None
    note = 0

    def __init__(self, nom):
        self.name = nom

    def aproved(self, note=None):
        if note:
            self.note = note

        if self.note >= 5:
            return True
        else:
            return False

    def print_name(self):
        print self.name

    def print_data(self):
        print "%s: %d" % (self.name, self.note)


class Abstracta(Clase):

    def __init__(self):
        super(Abstracta, self).__init__()
        self.name = "abstracta"


def sum(a, b):
    c = Clase('Manuel')
    c.note = 6

    c.aproved(7)

    return a+b