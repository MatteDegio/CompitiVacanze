def score(x, y):
    return ((x**2+y**2)**0.5 <=1)*5+((x**2+y**2)**0.5 <=5)*4+((x**2+y**2)**0.5 <=10)*1
