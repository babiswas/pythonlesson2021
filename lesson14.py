import random
class GiftShop:
    def __init__(self,**kwargs):
        self.gifts=dict()
        self.gifts.update(kwargs)

    @property
    def get_all_gifts(self):
        return self.gifts

    @get_all_gifts.setter
    def get_all_gifts(self,gifts):
        self.gifts.update(gifts)

    def get_your_gift(self,name,key):
        gift=self.gifts.get(key,None)
        if gift:
           return GiftShop.gift_message(name)+' '+gift
        elif not gift:
           return GiftShop.no_gift_message(name)

    @staticmethod
    def gift_message(name):
       return name+' '+"Here is your gift"

    @staticmethod
    def no_gift_message(name):
        return "Sorry"+' '+name+' '+"no gift for you"

    

if __name__=="__main__":
   g=GiftShop(one="Car",two="house",three="weapon")
   print(g.get_all_gifts)
   g.get_all_gifts={"four":"ball","five":"football"}
   print(g.get_all_gifts)
   while True:
      gift_key={1:"one",2:"two",3:"three",4:"four",5:"five"}
      random_key=random.choice([1,2,3,4,5,6,7,8,9,10])
      name=input("Enter your name:")
      key=gift_key.get(random_key,"sorry")
      print(g.get_your_gift(name,key))
   