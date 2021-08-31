def calcula_grado(num):
    if num>0.9 and num <=1:
        nota='A'
    elif num>0.8 and num <=0.9:
        nota='B'
    elif num >0.7 and num <=0.8:
        nota='C'
    elif num >0.6 and num <=0.7:
        nota='D'
    elif num <=0.6 and num >=0:
        nota='F'
    else:
        nota='score incorrecto'
    return nota
def main():
    #escribe tu código abajo de esta línea
    numero = float(input("Ingresa Un valor entre 0.0 y 1.0: "))
    nota=calcula_grado(numero)
    print(nota)

if __name__=='__main__':
    main()
