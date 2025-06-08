# a = input("Enter your oder:")
dic = {
    "pizza" : 24,
    "burger" : 90,
    "MOMO"  : 78,
    "soft_drinks" : 245
}
a = input("Enter your oder:")
if a in dic:
    print(f"order of {a} has been placed.it's bill is {dic[a]} rs.")

b = input("enter any more.(Y/N):")
if ( b == "Y"):
  c = input("enter your 2nd order:")
if c in dic: 
    print(f"second order {a} has been placed sir!")
    print("total bill is:",dic[a] + dic[c])

