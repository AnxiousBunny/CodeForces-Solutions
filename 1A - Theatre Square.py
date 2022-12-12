import math

indata = input() # n m a
data = indata.split(" ") #[n,m,a]

n = int(data[0])
m = int(data[1])
a = int(data[2])

i = n / a
j = m / a
print(math.ceil(i)*math.ceil(j))