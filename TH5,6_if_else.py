# Viet chuong trinh nhap vao 1 so nguyen tu ban phim, xuat ra ket qua so do chan hay le
print("is this number odd or even?")
x = int(input("Enter a value: "))
if x%2 == 0:
    print(f"{x} is a even number")
else:
    print(f"{x} is a odd number")

# Viet chuong trinh nhap vao diem trung binh mon, cho biet diem do thuoc loai kha, gioi, tb, yeu:
grades = float(input("Enter a grade: "))
if grades >= 9 and grades <=10:
    print("gioi")
elif grades >= 7 and grades < 9:
    print("kha")
elif grades >= 5 and grades <7:
    print("TB")
elif grades <5 and grades >=0:
    print("yeu")
