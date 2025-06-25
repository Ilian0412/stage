def moyenne(l):
    nombres = l 
    moyenne = sum(nombres) / len(nombres)
    return moyenne

def variance(l):
    m=moyenne(l)
    variance = [(i - m) ** 2 for i in l]
    return moyenne (variance) 

def ecartype(l):
    return variance(l)**0.5
