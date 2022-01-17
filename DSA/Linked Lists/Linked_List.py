class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None
    #   self.prevval = None


class SLL:
    def __init__(self):
        self.start=None



# class DLL:
#     def __init__(self):
#         self.start=None
#         self.end=None
  



list1 = SLL()
print (type(list1))
list1.start = Node ("1")
print (type(list1.start))
newdata= Node("2")
print(type(newdata))
newdata2= Node("3")

list1.start.nextval= newdata

newdata.nextval = newdata2


# newdata.prevval = list1.start
#identify platform
#API library 
#telegram bot BotFather .. bot api access token
# bot server hosting // replit

#music --yotube api --discord ko api

#Web Scrapping -- good beginner project
    #Website ko HTML DATA lai scrape
    #ncit website
    #replit //linux //import // pip //
        #  limited access
    
    
    #library beautifulsoup or scrappy














