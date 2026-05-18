# Viet chuong trinh nhap vao 1 nam duong lich, kiem tra nam do co phai nam nhuan hay khong?
year = int(input("Enter a year: "))

if (year % 4 == 0) or ((year % 400 == 0) and (year % 100 == 0)):
    print(f"{year} is nam nhuan")
else:
    print(f"{year} is not nam nhuan")
#Viet chuong trinh dem so ngay trong thang
month = -1
while (month <=- 0) or (month > 12):
    month = int(input("Enter a month: "))

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print(f"{month} has 31 days")
elif month==2 or month==4 or month==6 or month==9 or month==11:
    if month==2 and ((year % 4 == 0) or ((year % 400 == 0) and (year % 100 == 0))):
        print(f"{month} has 29 days")
    elif month == 2 and not ((year % 4 == 0) or ((year % 400 == 0) and (year % 100 == 0))):
        print(f"{month} has 28 days")