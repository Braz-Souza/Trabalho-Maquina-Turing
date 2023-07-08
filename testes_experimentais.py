from questao1 import maquina_questao_1
from questao2 import maquina_questao_2
from questao3 import maquina_questao_3
from questao4 import *

def testes_questao_1():
    assert maquina_questao_1([0,0,1,1]) == [1,0,1,1]
    assert maquina_questao_1([1,1,1,1,0,1]) == [0,0,0,0,1,1]
    assert maquina_questao_1([1,1,1,1,1,1,1]) == [0,0,0,0,0,0,0,1]
    assert maquina_questao_1([0]) == [1]
    assert maquina_questao_1([1]) == [0,1]
    print("Testes da primeira questao passaram com sucesso!")

def testes_questao_2():
    assert maquina_questao_2([]) == [1]
    assert maquina_questao_2([1]) == [1]
    assert maquina_questao_2([1, 1]) == [1]
    assert maquina_questao_2([1, 1, 1]) == []
    assert maquina_questao_2([1, 1, 1, 1]) == [1]
    assert maquina_questao_2([1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1]
    print("Testes da segunda questao passaram com sucesso!")

def testes_questao_3():
    assert maquina_questao_3([0]) == []
    assert maquina_questao_3([1, 0]) == [1]
    assert maquina_questao_3([0, 1]) == []
    assert maquina_questao_3([1, 0, 1]) == []
    assert maquina_questao_3([1, 1, 0, 1, 1]) == []
    assert maquina_questao_3([1, 1, 0, 1, 1, 1]) == []
    assert maquina_questao_3([1, 1, 1, 1, 1, 0, 1, 1]) == [1, 1, 1]
    print("Testes da terceira questao passaram com sucesso!")

def testes_questao_4():
    assert maquina_questao4_a(['#']) == True
    assert maquina_questao4_a([0, 1, '#', 1, 0]) == True
    assert maquina_questao4_a([0, 1, '#', 0, 1]) == False
    assert maquina_questao4_a([0, 1, '#', 1, 0, 0]) == False
    assert maquina_questao4_b(['a','a','b','b','c','c']) == True
    assert maquina_questao4_b(['a','a','b','b','c']) == True
    assert maquina_questao4_b(['a','b','b','c']) == False
    assert maquina_questao4_b(['a','b','b','c','c','c']) == False
    assert maquina_questao4_c(['a','b','c','c']) == True
    assert maquina_questao4_c(['a','b', 'b','c','c', 'c']) == True
    assert maquina_questao4_c(['a','b','c','c', 'c']) == False
    assert maquina_questao4_c(['a', 'a','b','c']) == False
    assert maquina_questao4_d([]) == True
    assert maquina_questao4_d(['a','b','c']) == True
    assert maquina_questao4_d(['a','a','b', 'c']) == False
    assert maquina_questao4_d(['a','b','b','c']) == False
    print("Testes da quarta questao passaram com sucesso!")

testes_questao_1()
testes_questao_2()
testes_questao_3()
testes_questao_4()