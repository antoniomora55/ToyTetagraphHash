

def encriptar(txt):
    a=0
    nuevo_bloque=""
    nuevo_bloque2=""
    nuevo_bloque3=""
    for x in texto:
       a+=1
       if(a<=16):
        nuevo_bloque+=x
       elif(a>=16 and a<=32):
        nuevo_bloque2+=x
       elif(a>=32 and a<=48):
        nuevo_bloque3+=x
       else:
        print("mensaje fuera de rango")
    print(nuevo_bloque)
    print("\n")
    print(nuevo_bloque2)
    print("\n")
    print(nuevo_bloque3)
        

print("Digite el texto a encriptar")
texto = input()
texto=texto.replace(" ","")
encriptar(texto)