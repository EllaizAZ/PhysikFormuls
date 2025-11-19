print("Силы:сила тока, гравитационная сила, сила упругости, сила трения, сила выталкивания ")
Formula =input("Введите формулу из предложенных: ")

#Про силы тока
if Formula == "сила тока":
    print("1- I=U/R ; 2- U=I*R ; 3- R=U/I")
    Formel_Cur=int(input())
    if Formel_Cur == 1:
        U=float(input("Напряжение: "))
        R=float(input("Сопротивление: "))
        I = U / R
        print(f'I = {I}')
    if Formel_Cur == 2:
        I=float(input("Сила: "))
        R=float(input("Сопротивление: "))
        U=I*R
        print(f'U = {U}')
    if Formel_Cur == 3:
        I = float(input("Силв: "))
        U = float(input("Напряжение: "))
        R = U/I
        print(f'R = {R}')
    else: print("неподходящая формула тока")

#гравитационная сила
if Formula == "гравитационная сила":
    print('F=G*(m1*m2)/r2')
    G=float(input("Гравитационная постаянная (google: 6,6743*10 (степень -11)H*m2/кг2): "))
    m1=float(input("Масса первого объекта (кг): "))
    m2 = float(input("Масса второго объекта (кг): "))
    r=float(input("растоянние между центрами масс (м): "))
    r2=r*r
    F = G * (m1 * m2) / r2
    print(f'F = {F}')

#Сила упругости
if Formula == "сила упругости":
    print("P(упр)=-kx")
    k=float(input("коэффициент жесткости H/m: "))
    x=float(input("удлинение(или сжатие) тела относительно его недеформированного положения(в метрах): "))
    F = k*x
    print(f'F = {F}')

#сила трения
#Обновление 2
