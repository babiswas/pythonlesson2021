from collections import defaultdict
from collections import OrderedDict


if __name__=="__main__":
   m=dict()
   m.update(key1="hello")
   m.update(key2="bello")
   m.update(key3="mello")
   print(m)
   del m["key1"]
   print(m)
   m.update(key4="tello")
   for key,value in m.items():
      print(key,value)
   print("Displaying value for keys")
   for key in m.keys():
      print(m.get(key,"Not present"))
   print(m.get("key8","Not present"))
   n=defaultdict(list)
   print(n.__missing__('a'))
   print(n.__missing__('b'))
   n['a'].append(1)
   n['a'].append(2)
   n['a'].append(3)
   print(n)
   val=OrderedDict()
   val['a']="hello"
   val['b']="bello"
   val['c']="tello"
   val['d']="mello"
   l=val.keys()
   k=m.keys()
   p=m.values()
   print(k)
   print(p)
   print(l)
   h={'a':1,'b':2}
   i={'m':5}
   print(h|i)

   