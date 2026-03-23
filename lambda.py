# Lambda function is a way to create an anonymous function tha we dont want to re-use


# ==================
# Example 1:
# ==================
def do_twice(m,n,fn):
    """Creates a function that runs twice"""
    return fn(fn(m,n),n)

print(do_twice(3,2, lambda x, p: x**p))

#Above, Lambda serves as a temporary function mapped to fn