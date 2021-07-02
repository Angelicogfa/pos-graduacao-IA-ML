import sys
sys.path.append('../../')

from behave import when, then
from configuration import getModel

modelFile = open("modelTeste.pkl", 'rb')
predictModel = getModel(modelFile).model()


@when("o usuário informa os dados '{sepal_length}' '{sepal_width}' '{petal_length}' '{petal_width}'")
def validaNome(context:object, sepal_length:float, sepal_width:float , petal_length:float , petal_width:float) -> None:
    context.sepal_length = sepal_length
    context.sepal_width = sepal_width
    context.petal_length = petal_length
    context.petal_width = petal_width


@then("o valor do metodo predict e o '{predict}'")
def validaFilmeRank(context:object, predict:float) -> None:
    assert float(predict) == predictModel.predict([[
        float(context.sepal_length), 
        float(context.sepal_width), 
        float(context.petal_length), 
        float(context.petal_width)
    ]])





