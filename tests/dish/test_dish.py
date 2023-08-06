from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    prato_1 = Dish('lasanha presunto', 25.90)
    prato_2 = Dish('lasanha presunto', 25.90)
    prato_3 = Dish('lasanha berinjela', 27.00)
    

    #2.1
    assert prato_1.name == "lasanha presunto"
    assert prato_2.name == "lasanha presunto"
    assert prato_3.name == "lasanha berinjela"

    #2.2 e 2.3
    assert hash(prato_1) == hash(prato_2)
    assert hash(prato_2) != hash(prato_3)

    #2.4 e 2.5
    assert (prato_1) == (prato_1)
    assert (prato_1) != (prato_3)

    #2.6
    assert repr(prato_1) == "Dish('lasanha presunto', R$25.90)"
    assert repr(prato_2) == "Dish('lasanha presunto', R$25.90)"
    assert repr(prato_3) == "Dish('lasanha berinjela', R$27.00)"

    #2.7
    with pytest.raises(TypeError):
        Dish('lasanha presunto', "Teste")

    #2.8
    with pytest.raises(ValueError):
        Dish('lasanha presunto', -25.90)

    #2.9
    prato_1.add_ingredient_dependency(Ingredient("ovo"), 5)
    assert prato_1.recipe == {Ingredient("ovo"): 5}

    #2.10
    assert prato_1.get_restrictions() == {Restriction.ANIMAL_DERIVED}

    #2.11
    assert prato_1.get_ingredients() == {Ingredient("ovo")}