from itertools import islice

obj=iter([1,2,3,4,5,6,7,8,9])
k=list()
while True:
   l=list(islice(obj,2))
   if not l:
      break
   else:
      k.append(l)
print(k)
