class Employee:
    def __init__(self, name):
        name = self.name
       
    def Speak(self, foods):
        print("heres ur order")
        
        
class Manager(Employee):
    def __init__(self, name):
        name = self.name
        
        
   


class Stock:
    def __init__(self, itemsInStock):
        itemsInStock = self.itemsInStock
       
    def AddItemToStock(self,item):
        itemsInStock[item] += 1
       
    def RemoveItemFromStock(self, item):
        if(item in itemsInStock and itemsInStock[item] > 0):
            itemsInStock[item] -= 1
        else:
            return

       

       
    def ReturnInfo(self):
        return self.name, self.price
   
class Item:
    def __init__(self, name, price, nutrition):
         self.name = name
         self.price = price
         self.nutrition = nutrition
         
    def GetOrder(self):
        return self.name, self.price, self.nutrition
    
    
    
         
class Nutrition:
    def __init__(self, calories, protein, sugars):
        self.calories = calories
        self.protein = protein
        self.sugars = sugars
    def GetNutrition(self):
        return self.calories, self.protein, self.sugars
    def SetNutrition(self, calories, protein, sugars):
        self.calories = calories
        self.protein = protein
        self.sugars = sugars
        
    def AddToNutrition(self, calories, protein, sugars):
        self.calories += calories
        self.protein += protein
        self.sugars += sugars
    

       
class Order:
    def __init__(self):
        self.order = []

    def AddItemToOrder(self, itemToAdd):
        self.order.append(itemToAdd)

    def DisplayOrderDetails(self):
        stringToDisplay = "Here's your order of a "
        priceOfOrder = 0
        nutritionOfOrder = Nutrition(0, 0, 0)

        for item in self.order:
            priceOfOrder += float(item.GetOrder()[1])
            nutrition = item.GetOrder()[2].GetNutrition()
            nutritionOfOrder.AddToNutrition(float(nutrition[0]), float(nutrition[1]), float(nutrition[2]))
            stringToDisplay += f"{item.GetOrder()[0]}, "  # Assuming this gets item name or similar

        nutritionSummary = nutritionOfOrder.GetNutrition()
        stringToDisplay += f"\nThis meal has {nutritionSummary[0]} calories, {nutritionSummary[1]} grams of protein and {nutritionSummary[2]} grams of sugar. It will cost you ${priceOfOrder}"

        print( stringToDisplay)


file = open('data.csv','r')

menu = file.readlines()
menu[0].replace('\n','').split(",")

itemsOnMenu = []

for item in menu:
    itemsOnMenu.append(item.replace('\n','').split(","))
   
mainMenuInObjects = []

for item in itemsOnMenu:
    mainMenuInObjects.append(Item(item[0],item[1], Nutrition(item[2],item[3],item[4])))
   

   
   


print(itemsOnMenu)
print(mainMenuInObjects)
       

#name,averagePrice,calories,protein,sugar


