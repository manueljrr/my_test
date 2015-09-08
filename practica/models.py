__author__ = 'Manuel'

from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=30, help_text="Nombre del producto")
    descripcion = models.CharField(max_length=255, help_text="Una descripcion que nos ayude a identificar el producto")
    stock = models.BooleanField(default=False)
    codigo = models.IntegerField(max_length=6)
    cantidad = models.IntegerField(max_length=3)


class Transaccion(models.Model):

    #def next_order():
    #    next_order = Transaccion.objects.count() + 1
    #    return str(next_order).zfill(10)

    order = models.CharField(max_length=10, editable=False)

    def __init__(self):
        super(Transaccion, self).__init__()
        next_order = Transaccion.objects.count() + 1
        self.order = str(next_order).zfill(10)



class Venta(Transaccion):
    monto = models.FloatField(default=0)


class Animal(object):
    def eat(self):
        pass

class LandAnimal(Animal):
    def walk(self):
        pass

class Monkey(LandAnimal):
    def climb_trees(self):
        pass

class Dog(LandAnimal):
    def bark(self):
        pass

class Bird(Animal):
    def fly(self):
        pass

class Parrot(Bird):
    def imitate_voice(self):
        pass

class Eagle(Bird):
    def kill(self):
        pass


import collections
def highest_count_letters(word):
    counts = collections.Counter(word)
    highest = max(counts.itervalues())

    for k, v in counts.iteritems():
        if v==highest:
            print k, v

def read_csv_to_array(path):
    import csv
    datafile = open('a.csv', 'r')
    datareader = csv.reader(datafile, delimiter=';')
    data = []
    for row in datareader:
        data.append(row)

def read_csv_to_array(path):
    array = []
    with open(path) as data_file:
        for line in data_file:
            array.append(line.strip().split(','))

    array[0].append('Total')
    for row in array[1:len(array)]:
        row[2] = int(row[2])
        row[3] = float(row[3])
        row.append(row[2]*row[3])

    return array
