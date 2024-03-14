from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredientA = Ingredient("salmão")
    ingredientB = Ingredient("salmão")
    ingredientC = Ingredient("farinha")

    assert ingredientA == ingredientB
    assert ingredientA != ingredientC

    assert hash(ingredientA) == hash(ingredientB)
    assert hash(ingredientB) != hash(ingredientC)

    assert ingredientA.name == "salmão"

    assert repr(ingredientA) == "Ingredient('salmão')"

    assert ingredientA.restrictions == {
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }
