def round(x):
    z = str(x)
    for i in range(len(z)):
        if z[i] == '.' and z[i+1] != '0':
            y = x//1 + 1
            break
        else:
            y = x
    return y

print(round(2.2))

def floor(x):
    return x//1
print(floor(2.111111))