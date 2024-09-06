"""
CSE 2120: Data Structures
*args & **kwargs

"""

# Complete this function only...

def temperature(**kwargs):
    return dict(kwargs)


# DO NOT EDIT any of the code below.

def main():
    print(temperature(C=0))  # {'C':0, 'K':273.15, 'F':32}
    print(temperature(F=68))  # {'C':20, 'K':293.15, 'F':68}
    print(temperature(K=77))  # {'C':-196.15, 'K':77, 'F':-321.07}

main()
