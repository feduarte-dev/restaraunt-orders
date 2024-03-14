import csv

from models.dish import Dish, Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:

        with open(source_path, encoding="utf-8") as file:
            reader = csv.DictReader(file)
            dishes_dict = dict()

            for row in reader:
                dish_name = row["dish"]
                if dish_name not in dishes_dict:
                    dishes_dict[dish_name] = Dish(
                        dish_name, float(row["price"])
                    )

                dishes_dict[dish_name].add_ingredient_dependency(
                    Ingredient(row["ingredient"]),
                    int(row["recipe_amount"]),
                )

        self.dishes = set(dishes_dict.values())
