def maquina_questao_1(x, estado_atual='q0', i=0):
    if estado_atual == 'q0':
        if len(x) == i:
            x.append(1)
            i += 1
            novo_estado = 'q1'
            return maquina_questao_1(x, novo_estado, i)
        if x[i] == 1:
            x[i] = 0
            i += 1
            novo_estado = 'q0'
            return maquina_questao_1(x, novo_estado, i)
        if x[i] == 0:
            x[i] = 1
            i += 1
            novo_estado = 'q1'
            return maquina_questao_1(x, novo_estado, i)
    return x