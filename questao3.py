def remover_none_em_lista(lista):
    lista = list(filter(lambda x: x != None, lista))
    return lista

def maquina_questao_3(fita, estado_atual='q0', i=0):
    if estado_atual == 'q0':
        if fita[i] == 0:
            return maquina_questao_3(fita, 'q1', i + 1)
        if fita[i] == 1:
            return maquina_questao_3(fita, 'q0', i + 1)
    if estado_atual == 'q1':
        if len(fita) == i:
            return maquina_questao_3(fita, 'q2', i - 1)
        if fita[i] == "X":
            return maquina_questao_3(fita, 'q1', i + 1)
        if fita[i] == 1:
            fita[i] = "X"
            return maquina_questao_3(fita, 'q6', i + 1)
    if estado_atual == 'q2':
        if fita[i] == "X":
            fita.pop(i)
            return maquina_questao_3(fita, 'q2', i - 1)
        if fita[i] == 0:
            fita.pop(i)
            return maquina_questao_3(fita, 'q3', i - 1)
    if estado_atual == 'q3':
        fita = remover_none_em_lista(fita)
        return fita
    if estado_atual == 'q4':
        if fita[i] == None:
            return maquina_questao_3(fita, 'q4', i + 1)
        if fita[i] == 1:
            return maquina_questao_3(fita, 'q4', i + 1)
        if fita[i] == 0:
            return maquina_questao_3(fita, 'q1', i + 1)
    if estado_atual == 'q5':
        if i < 0:
            return maquina_questao_3(fita, 'q7', i + 1)
        if fita[i] == None:
            return maquina_questao_3(fita, 'q7', i + 1)
        if fita[i] == 1:
            return maquina_questao_3(fita, 'q5', i - 1)
    if estado_atual == 'q6':
        if len(fita) == i:
            return maquina_questao_3(fita, 'q6', i - 1)
        if fita[i] == 1:
            return maquina_questao_3(fita, 'q6', i - 1)
        if fita[i] == "X":
            return maquina_questao_3(fita, 'q6', i - 1)
        if fita[i] == 0:
            return maquina_questao_3(fita, 'q5', i - 1)
    if estado_atual == 'q7':
        if fita[i] == 1:
            fita[i] = None
            return maquina_questao_3(fita, 'q4', i + 1)
        if fita[i] == 0:
            return maquina_questao_3(fita, "q1", i + 1)
    