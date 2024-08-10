
class Eatable:
    def __init__(self, carbs, fat, protein) :
        self.carbs = carbs
        self.protein = protein
        self.fat = fat
        
    def food_type(self):
        print("Eatable items")
    
    
class Vegetarian(Eatable):
    def __init__(self, carbs, fat, protein, isPeelable):
        super().__init__(carbs, fat, protein)
        self.isPeelable = isPeelable

    def food_type(self):
        print("Vegitable type")

class Non_veg(Eatable):
    def __init__(self, carbs, fat, protein, isBoneless):
        super().__init__(carbs, fat, protein)
        self.isboneless = isBoneless
        
    def food_type(self):
        print("Non vegitable type")
        
carbs = int(input('Enter Carbs '))
fat = int(input('Enter fat '))
protein = int(input('Enter Protein '))
isPeelable = (input('Is it isPeelable yes or no  ')).lower()
isBoneless = (input('Is it isBoneless yes or no  ')).lower() 

veg = Vegetarian(carbs,fat,protein,isPeelable)  
veg.food_type()

nonveg = Non_veg(carbs,fat,protein,isBoneless)  
nonveg.food_type()