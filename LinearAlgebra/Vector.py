from math import sqrt


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def magnitude(self):
        coordinates_squared = [x ** 2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1/magnitude)
        except ZeroDivisionError:
            Exception('Cannot normalize the zero vector')

    def times_scalar(self, multiplier):
        return [x * multiplier for x in self.coordinates]
    
    def hello_print(self):
        print('hello')

    def dot(self, v)
        return sum([x * y for x,y in zip(self.coordinates, v.coordinates)])
    
        def angle_with()

#TODO(yigit): code quiz 8

    #def dot_product(self, otherVector):
        #dot_p = Vector(self)
        #if len(self.coordinates) == len(otherVector.coordinates):
        #    for i in xrange(len(self.coordinates)):
        #        dot_p[i] = [self.coordinates[i] * otherVector.coordinates[i]]
        #return dot_p

my_vector = Vector([3, 4])

print my_vector.magnitude()
print my_vector.normalized()
