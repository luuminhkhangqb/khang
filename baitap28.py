#Bài 1: Kiểm tra số chẵn, số lẻ
a=int(input("Mời bạn nhập một số"))
if(a % 2 == 0):
    print(a, "là số chẵn")
else:
    print(a,"là số lẻ")
#Bài 2: In ra dãy số từ 0 đến n
n=int(input("Nhập một số:"))
dem=0
while (dem <= n):
    print (dem)
    dem += 1
#Bài 3: Tổng dãy số
a = int(input("Nhập một số"))
b=1
tong = 0
while (b <= a):
    tong += b 
    b += 1
    print ("Tổng là:", tong)
#Bài 4: In ra bảng cửu chương 
a = int(input("Nhập một số"))
b=1
while(b <= 10):
    c = a * b
    print (f"{a} * {b} = {c}")
    b += 1
#Bài 5: Tìm số chẵn số đó và tính tổng các số chẵn
a = int (input("Nhập vào một số:"))
s=0
while a>0:
    if (a%10)%2==0:
        print(a%10)
        s+=a%10
    a//=10
print(s)
   