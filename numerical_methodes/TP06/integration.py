import math

def simpson(f,a:float,b:float,n:int):
    I=0
    h=(b-a)/n
    s1=0
    s2=0
    for i in range(1,n):
        xi = a + (i*h)
        s1 = s1 + f(xi)
    for i in range(n):
        xi = a + (i*h)
        xii = xi + h
        s2 = s2 + f((xi+xii)/2)
    I = (h/6)*(f(a)+f(b)+2*s1+4*s2)
    return I


def simpson_re(f,a:float, b:float,n:int,i=1,s1=0,s2=0):
    h = (b-a)/n
    if i == n:
        xi=a 
        xii= xi+h
        s2 =s2+ f((xi+xii)/2)
        return (h/6)*(f(a)+f(b)+2*s1+4*s2)
    else:
        xi=a +(i*h)
        s1=s1+f(xi)
        xi=a +(i*h)
        xii=xi+h
        s2=s2 +f((xi +xii)/2)
        return simpson_re(f,a,b,n,i+1,s1,s2) 

def simpson2(f : list,a:float,b:float,n:int):
    I=0
    h=(b-a)/n
    s1=0
    s2=0
    for i in range(2,n,2):
        s1 = s1 + f[i][1]
    for i in range(1,n,2):
        s2 = s2 + f[i][1]
    I = (h/3)*(f[0][1]+f[-1][1]+2*s1+4*s2)
    return I


def trapez(f,a : float,b : float,n : int):
    I = 0
    h = (b-a)/n
    S = 0
    for i in range(1,n):
        xi = a + (i*h)
        S += f(xi)
    I = h*((f(a)+f(b))/2+S)
    return I

def re_trapez(f,a : float,b : float,n : int,i=1,I=0.0):
    h = (b-a)/n
    if n == i:
        return h*((f(a)+f(b))/2+I)
    xi = a + (i*h)
    I += f(xi) 
    return re_trapez(f=f,a=a,b=b,n=n,i=i+1,I=I)


def methodeRectG(func,a,b,n):
    I = 0
    h = (b-a)/n
    s = 0
    for i in range(0,n) :
        x = a + (i*h)
        s = s + func(x)
    I = h * s
    return I

def methodeRectM(func,a,b,n):
    I = 0
    h = (b-a)/n
    s = 0
    for i in range(1,n+1) :
        x = a + (i + 0.5) * h
        s = s + func(x)
    I = h * s
    return I

def methodeRectD(func,a,b,n):
    I = 0
    h = (b-a)/n
    s = 0
    for i in range(1,n+1) :
        x = a + (i*h)
        s = s + func(x)
    I = h * s
    return I

def func1(x):
    return 1/x
def dirivee(x):
    return -1/x**2
def errrAbs(a,b):
    return abs(a-b)
def errsupRect(m1,n,a,b):
    return  (m1*(b-a)**2)/((2*n))
def errsupTrap(m2,n,a,b):
    return (b-a)**3 * m2 / (12 * n**2)
def errsupSimp():
    return 0
def trnRect(m1,err,a,b):
    return (m1 *(b-a)**2)/(2 * err)  
def trnTrap(m2,err,a,b):
    return math.sqrt((b-a)**3 *m2 / (12 * err))

def errsupSimp(class_fonction, function_derive, a, b, n):
    if class_fonction == 4:
        M4 = max(abs(function_derive(a)), abs(function_derive(b)))
        return (M4 / (180 * (n**4))) * ((b - a)**5)
    else:
        M3 = max(abs(function_derive(a)), abs(function_derive(b)))
        return (M3 / (90 * (n**3))) * ((b - a)**4)


def menu_trapez():
    def f1(x):
        return math.cos(x**2) 
    
    print("\n=========== Integration ==============")
    print("\nfonction : cos(x**2) dans l interval [0,1]")
    print("Iexact = 0.9045 ")
    Iexact = 0.9045
    m2 = 3.844
    a = 0
    b = 1
    
    print("1. Trapez iterative : ")
    print("2. Trapez recurvive : ")
    print("3. trouver n")

    choix =  input("\n choisire la methode du calcule : ")


    if(choix == '1'):
        n = input("Donner le nombre du points a utuliser dans les calcules : ")
        n = int(n)
        err = errsupTrap(a=a,b=b,m2=m2,n=n)
        print(f"err superieur : {err}")
        I = trapez(f=f1,a=a,b=b,n=n)
        print(f"avec n={Iexact} l = \033[96m  {I} \033[0m ")
        print(f"err absolute {errrAbs(Iexact,I)}")
    elif(choix == '2'):
        n = input("Donner le nombre du points a utuliser dans les calcules : ")
        n = int(n)
        err = errsupTrap(m2=m2,n=n)
        print(f"err superieur : {err}")
        I = re_trapez(f=f1,a=a,b=b,n=n)
        print(f"avec n={Iexact} l = \033[96m  {I} \033[0m ")
        print(f"err absolute {errrAbs(Iexact,I)}")
    elif(choix == '3'):
        err = float(input("Donner l'erreur :  "))
        n = trnTrap(a=a,b=b,m2=m2,err=err)
        print(f"la borne superieur est : \033[96m  {n} \033[0m ")
    







def menu_rectangle():
    a= 1
    b = 2
    n = 10
    #1
    I = methodeRectG(func1,a,b,n)
    print(f"integral est avec method rectangles gauch :  {I}")


    #2
    Ir = math.log(2)
    errr = errrAbs(Ir,I)
    print(f"l erreur abs G : {errr}")
    #3
    m1 = 1
    errs = errsupRect(m1,n,a,b)
    print(f"erreur sup G {errs}")

    print("\n\n")


    #1
    ID = methodeRectD(func1,a,b,n)
    print(f"integral est avec method rectangles droit :  {ID}")

    #2
    Ir = math.log(2)
    errr = errrAbs(Ir,ID)
    print(f"l erreur abs D : {errr}")
    #3
    m1 = 1
    errs = errsupRect(m1,n,a,b)
    print(f"erreur sup D {errs}")

    print("\n\n")

    IM = methodeRectM(func1,a,b,n)
    print(f"integral est avec method rectangles milieu :  {IM}")


    #2
    Ir = math.log(2)
    errr = errrAbs(Ir,IM)
    print(f"l erreur abs M : {errr}")
    #3
    m1 = 1
    errs = errsupRect(m1,n,a,b)
    print(f"erreur sup M {errs}")



    #4
    err = 0.001
    ne =  trnRect(m1,err,a,b)
    print(f"le nombre d éteration max pout un err {err} est : {ne}")

def saisie_tableau():
    n = 0
    n=  int(input("donner de nomberdes  valeurs du tableau (0 pout quitter ):"))
    valeurs = []
    for i in range(0,n):
        x = float(input("donner x :"))
        fx = float(input("donner fx :"))
        valeurs.append((x,fx))
    return valeurs


 

def menu_simpson():
    def fun(x):
        return 1/(1+x**2)
    def dirivee4(x):
        return 24*(5*x**4-10*x**2+ 1) /(1+x**2)**5
    
    print("\n=========== Integration ==============")
    print("== metode de simpson f(x) =  1/(1+x**2) dans l'intervale [0,3]")
    n = 6
    I = simpson(fun,0,3,n)
    print(f"la valeur de simpson : \033[96m {I} \033[0m\n valeur exact {math.atan(3)}")
    print(f"simpson recursive \033[96m {simpson_re(f=fun,a=0,b=3,n=n)} \033[0m")
    print(f"\nerrsup : {errsupSimp(4,dirivee4,0,3,n)}")
    print(f"errabs : {errrAbs(I,errrAbs(I,math.atan(3)))}")

    print("\n\n== simpson tableaux (exemple)")
   
    vitess = [(0,30),(10,31.63),(20,33.44),(30,35.47),(40,37.75),(50,40.33),(60,43.29),(70,46.70),(80,50.67)]
    print("metode de simpson ",vitess)
    I = simpson2(vitess,0,80,8)
    print(f"la valeur de simpson :\033[96m  {I} \033[0m")


    print("\n\n== simpson tableaux donner votre exemple")
    valeurs = saisie_tableau()
    if(len(valeurs) != 0):
        print("valeurs : ",valeurs)
        I = simpson2(valeurs,valeurs[0][1],valeurs[-1][1],len(valeurs))
        print(f"la valeur de simpson :  {I}")


if __name__ == "__main__":
    menu_simpson()