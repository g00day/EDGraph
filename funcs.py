

def I(t):
    """ Сила тока """
    q = float(input("q "))
    return q * t

def Q(t):
    """ Заряд """ 
    I = float(input("I "))
    return I * t
    
def E(t):
    """ Энергия катушки """
    return I(t) ** 2 / 2

def W(t):
    """ Энергия конденсатора """
    U = float(input("U "))
    return (Q(t) * U) / 2
