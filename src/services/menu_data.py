from models.dish import Dish
from models.ingredient import Ingredient
import csv

# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self._recipes = []
        self.dishes: Dish = set()

        with open(source_path, "r") as file:
            reader = csv.reader(file)
            header, *rows = reader
            self._recipes = rows

        dishes_list = dict()
        
        for dish, price, ingredient, recipe_amount in self._recipes:
            if dish not in dishes_list:
                dishes_list[dish] = Dish(dish, float(price))
            dishes_list[dish].add_ingredient_dependency(Ingredient(ingredient), int(recipe_amount))

        self.dishes.update(dishes_list.values())