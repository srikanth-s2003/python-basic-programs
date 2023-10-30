def simpleInterest(p, t, t):
  return (p*t*r)//100

p = int(input("Enter the principle amount:"))
t = int(input("Enter duration/time:"))
r = int(input("Enter rate of return:"))
SI = simpleInterest(p, t, r)
print('SIMPLE INTEREST :',SI)
