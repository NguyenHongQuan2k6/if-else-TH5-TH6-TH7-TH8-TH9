# giai phuong trinh bac 2
a = float(input("He so a: "))
b = float(input("He so b: "))
c = float(input("He so c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("Phuong trinh vo nghiem")
elif delta == 0:
    print("Phuong trinh co nghiem kep x1 = x2 = ",-b/2*a)
else:
    print("Phuong trinh co 2 nghiem phan biet: ", "x1 = ",(-b+(delta)**(1/2))/2*a,",","x2 = ",(-b-delta**(1/2))/2*a)