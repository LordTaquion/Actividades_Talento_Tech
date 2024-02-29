# Realizado por Jairo Andres Sánchez

def supra(x):
    
    x = x.lower()
    c = {}

    for i in x:
        c[i] = c.get(i, 0) + 1

    s = set(x)
    r = sorted(s)
    
    print("Aqui hay un listado de las letras de la palabra y cuantas veces aparece en ella: ")
    for h in r:
        print(f"{h}: {c[i]}")

    print ("Estos son las letras de la palabra en orden alfabético: ")
    print (r)

supra("EsternocleiDomasToideo")