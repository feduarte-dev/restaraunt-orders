from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    recipeA = Dish("Recipe A", 10.99)
    recipeB = Dish("Recipe A", 10.99)
    recipeC = Dish("Recipe C", 12.99)
    assert recipeA.name == "Recipe A"

    ingredientA = Ingredient("Ingredient A")
    recipeA.add_ingredient_dependency(ingredientA, 3)
    assert recipeA.get_ingredients() == {Ingredient("Ingredient A")}

    assert recipeA == recipeB

    assert recipeA.get_restrictions() == set()

    assert hash(recipeA) == hash(recipeB)
    assert hash(recipeA) != hash(recipeC)

    assert repr(recipeA) == "Dish('Recipe A', R$10.99)"

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Recipe D", "10.00")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("Recipe E", -10.00)
