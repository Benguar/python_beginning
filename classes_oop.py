# Classes are used to create your own data types they are made up of 2 things data values that make up the class e.g co-ordinates are made up of 2 integers and attributes what the data can do


# Methods are functions that only works with classes


# ================
# Example 1a creating an data type co-ordinate
# ================


class coordinate(object):
    def __init__(
        self, xval, yval
    ):  # this is a method self is a way to refer to an object of this data type without actually creating one. it is used to represent data since we do not have an actual data yet we are only defining it
        self.x = xval  # this is used to attach the x variable of the self to xval creating a data attribute .x
        self.y = yval  # this is used to attach the y variable of the self to yval creating a data attribute .y

    # now we create a method that calculates the distance between 2 points
    def distance(
        self, other
    ):  # the other must be a parameter of the same data type in this case data type coordinate since we are going to be using the x and y parameters of object also object is a variable it can be represented with anything else
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    def origin(self):
        self.x = 0
        self.y = 0


# This is an instance of actual use of object coordinate we created
c = coordinate(
    1, 2
)  # here we reference the name of the class and we put in values to represent the 2 values we initialized. xval and yval self here now becomes (1,2)
origin = coordinate(0, 0)


# print(c.x) #this is used to access the x data attribute of the coordinate since we have already initialized  it in our init method to access it we just need to call the attribute name in this case it is .x it can also be .y since we defined .x and .y and attached vak=lues to them


# TO use the method distance.  we use it in a similar way of list.append(3) e.g

# print(c.distance(origin)) #here, the origin becomes  object in the distance function in the class coordinate c also becomes self in the distance function
# print(coordinate.distance(c,origin)) #this is another way to call a method
c.origin()
# print(c.y)

# ================
# Example 1b creating a class circle with parameters radius and coordinates
# ================


class circle(object):
    def __init__(self, radius=int, coordinates=coordinate):
        if type(radius) == int:
            self.radius = radius
        if type(coordinates) == coordinate:
            self.center = coordinates

    def circumference(self):
        return 2 * self.radius * (22 / 7)

    def area(self):
        return (22 / 7) * (self.radius**2)

    def in_circle(self, point):
        return self.center.distance(point) < self.radius


# circle = circle(1,coordinate(2,7))
# print(circle.center.x)
# p = coordinate(1,1)
# print(circle.in_circle(p))

# ================
# Example 2 creating an data type fraction
# ================


class fraction(object):
    def __init__(self, numerator=int, denominator=int):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(
        self,
    ):  # This sets how fraction class should be printed it is a dunder method __str__
        if self.denominator != 1:
            return f"{self.numerator}/{str(self.denominator)}"
        else:
            return f"{self.numerator}"

    def __mul__(self, object):  # this is the dunder method for the operation *
        numerator = self.numerator * object.numerator
        denominator = self.denominator * object.denominator
        if numerator / denominator == 1:
            return fraction(numerator, denominator)
        else:
            return fraction(numerator, denominator)
    def __float__(self): #this is the dunder method for floats
        return self.numerator/self.denominator
    
    def multiply_fraction(self, object):
        numerator = self.numerator * object.numerator
        denominator = self.denominator * object.denominator
        if numerator / denominator == 1:
            print(numerator / denominator)
            return fraction(numerator, denominator)
        else:
            print(f"{numerator}/{denominator}")
            return fraction(numerator, denominator)

    def divide_fraction(self, object):
        numerator = self.numerator * object.denominator
        denominator = self.denominator * object.numerator
        if numerator / denominator == 1:
            print(numerator / denominator)
            return fraction(numerator, denominator)
        else:
            print(f"{numerator}/{denominator}")
            return fraction(numerator, denominator)

    def inverse(self):
        return 1 / (self.numerator / self.denominator)

    def invert(self):
        x = self.numerator
        self.numerator = self.denominator
        self.denominator = x


f1 = fraction(1, 2)
f2 = fraction(3, 2)
print(f1 * f2)
print(float(f1))
ans = f1.divide_fraction(f2)
print(f1.inverse())
f1.invert()
print(f1.numerator, f1.denominator)
