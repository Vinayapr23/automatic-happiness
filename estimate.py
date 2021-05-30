
def wallis(n):
  pi =2;
  for i in range(1,n):
    value = float(4* i**2 /(4*i**2-1))
    pi =pi*value
   return pi
  
