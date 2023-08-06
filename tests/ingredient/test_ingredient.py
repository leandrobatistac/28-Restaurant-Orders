from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingrediente_1 = Ingredient('farinha')
    ingrediente_2 = Ingredient('farinha')
    ingrediente_3 = Ingredient('ovo')
    

    #1.1 e 1.2
    assert hash(ingrediente_1) == hash(ingrediente_2)
    assert hash(ingrediente_1) != hash(ingrediente_3)

    #1.3 e 1.4
    assert (ingrediente_1) == (ingrediente_1)
    assert (ingrediente_1) != (ingrediente_3)

    #1.5
    assert repr(ingrediente_1) == "Ingredient('farinha')"

    #1.6
    assert ingrediente_1.name == "farinha"

    #1.7
    restrictions_test = {Restriction.GLUTEN}
    assert (ingrediente_1).restrictions == restrictions_test