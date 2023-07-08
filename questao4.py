def maquina_questao4_a(fita, estado_atual='q0', i=0):
    if estado_atual == 'q0':
        if fita[i] == 0:
            fita[i] = None
            return maquina_questao4_a(fita, 'q2', i + 1)
        if fita[i] == 1:
            fita[i] = None
            return maquina_questao4_a(fita, 'q4', i + 1)
        if fita[i] == "#":
            return maquina_questao4_a(fita, 'q6', i + 1)
    if estado_atual == 'q2':
        if len(fita) == i:
            return maquina_questao4_a(fita, 'q3', i - 1)
        if fita[i] == None:
            return maquina_questao4_a(fita, 'q3', i - 1)
        if fita[i] == "#" or fita[i] == 1 or fita[i] == 0:
            return maquina_questao4_a(fita, 'q2', i + 1)
    if estado_atual == 'q4':
        if len(fita) == i:
            return maquina_questao4_a(fita, 'q5', i - 1)
        if fita[i] == None:
            return maquina_questao4_a(fita, 'q5', i - 1)
        if fita[i] == "#" or fita[i] == 1 or fita[i] == 0:
            return maquina_questao4_a(fita, 'q4', i + 1)
    if estado_atual == 'q3':
        if fita[i] == 0:
            fita[i] = None
            return maquina_questao4_a(fita, 'q1', i - 1)
    if estado_atual == 'q5':
        if fita[i] == 1:
            fita[i] = None
            return maquina_questao4_a(fita, 'q1', i - 1)
    if estado_atual == 'q1':
        if i < 0:
            return maquina_questao4_a(fita, 'q0', i+1)
        if fita[i] == None:
            return maquina_questao4_a(fita, 'q0', i + 1)
        if fita[i] == "#" or fita[i] == 1 or fita[i] == 0:
            return maquina_questao4_a(fita, 'q1', i - 1)
    if estado_atual == 'q6':
        return True
    return False

def maquina_questao4_b(fita, estado_atual='q0', i=0):
    if estado_atual == 'q0':
        if len(fita) == i:
            return maquina_questao4_b(fita, 'q8', i + 1)
        if fita[i] == 'a':
            fita[i] = 'A'
            return maquina_questao4_b(fita, 'q1', i + 1)
        if fita[i] == 'c':
            return maquina_questao4_b(fita, 'q9', i + 1)
        if fita[i] == 'b':
            fita[i] = 'D'
            return maquina_questao4_b(fita, 'q4', i + 1)
    if estado_atual == 'q1':
        if len(fita) == i:
            return maquina_questao4_b(fita, 'q2', i - 1)
        if fita[i] == 'B' or fita[i] == 'c':
            return maquina_questao4_b(fita, 'q2', i - 1)
        if fita[i] == 'a' or fita[i] == 'b':
            return maquina_questao4_b(fita, 'q1', i + 1)
    if estado_atual == 'q2':
        if fita[i] == 'A' or fita[i] == 'a':
            return maquina_questao4_b(fita, 'q3', i + 1)
        if fita[i] == 'b':
            fita[i] = 'B'
            return maquina_questao4_b(fita, 'q12', i - 1)
    if estado_atual == 'q3':
        if len(fita) == i:
            return maquina_questao4_b(fita, 'q8', i + 1)
        if fita[i] == 'a':
            return maquina_questao4_b(fita, 'q3', i + 1)
        if fita[i] == 'B':
            fita[i] = 'D'
            return maquina_questao4_b(fita, 'q4', i + 1)
    if estado_atual == 'q4':
        if len(fita) >= i:
            return maquina_questao4_b(fita, 'q5', len(fita) - 1)
        if fita[i] == 'C':
            return maquina_questao4_b(fita, 'q5', i - 1)
        if fita[i] == 'B' or fita[i] == 'c' or fita[i] == 'b':
            return maquina_questao4_b(fita, 'q4', i + i)
    if estado_atual == 'q5':
        if fita[i] == 'c':
            fita[i] = 'C'
            return maquina_questao4_b(fita, 'q6', i - 1)
    if estado_atual == 'q6':
        if fita[i] == 'B' or fita[i] == 'b' or fita[i] == 'c':
            return maquina_questao4_b(fita, 'q6', i - 1)
        if fita[i] == 'D':
            return maquina_questao4_b(fita, 'q7', i + 1)
    if estado_atual == 'q7':
        if fita[i] == 'C':
            return maquina_questao4_b(fita, 'q8', i + 1)
        if fita[i] == 'b' or fita[i] == 'B':
            fita[i] = 'D'
            return maquina_questao4_b(fita, 'q6', i + 1)
    if estado_atual == 'q8':
        return True
    if estado_atual == 'q9':
        if len(fita) == i:
            return maquina_questao4_b(fita, 'q8', i + 1)
        if fita[i] == 'c':
            return maquina_questao4_b(fita, 'q9', i + 1)
    if estado_atual == 'q10':
        if len(fita) == i:
            return maquina_questao4_b(fita, 'q8', i - 1)
        if fita[i] == 'B' or fita[i] == 'c':
            return maquina_questao4_b(fita, 'q10', i + 1)
    if estado_atual == 'q11':
        if fita[i] == 'B':
            return maquina_questao4_b(fita, 'q10', i + 1)
        if fita[i] == 'a':
            fita[i] = 'A'
            return maquina_questao4_b(fita, 'q1', i + 1)
        if fita[i] == 'b':
            fita[i] = 'D'
            return maquina_questao4_b(fita, 'q4', i + 1)
    if estado_atual == 'q12':
        if fita[i] == 'a' or fita[i] == 'b':
            return maquina_questao4_b(fita, 'q12', i - 1)
        if fita[i] == 'A':
            return maquina_questao4_b(fita, 'q11', i + 1)
    return False

def maquina_questao4_c(fita, estado_atual='q0', i=0):
    if estado_atual == 'q0':
        if len(fita) == i:
            return maquina_questao4_c(fita, 'q5', i + 1)
        if fita[i] == 'a' or fita[i] == 'b':
            fita[i] = 'X'
            return maquina_questao4_c(fita, 'q1', i + 1)
    if estado_atual == 'q1':
        if len(fita) == i:
            return maquina_questao4_c(fita, 'q2', i - 1)
        if fita[i] == 'X':
            return maquina_questao4_c(fita, 'q2', i - 1)
        if fita[i] == 'a' or fita[i] == 'b' or fita[i] == 'c':
            return maquina_questao4_c(fita, 'q1', i + 1)
    if estado_atual == 'q2':
        if fita[i] == 'c':
            fita[i] = 'X'
            return maquina_questao4_c(fita, 'q3', i - 1)
    if estado_atual == 'q3':
        if fita[i] == 'c':
            return maquina_questao4_c(fita, 'q4', i - 1)
        if fita[i] == 'X':
            return maquina_questao4_c(fita, 'q5', i - 1)
    if estado_atual == 'q4':
        if fita[i] == 'a' or fita[i] == 'b' or fita[i] == 'c':
            return maquina_questao4_c(fita, 'q4', i - 1)
        if fita[i] == 'X':
            return maquina_questao4_c(fita, 'q0', i + 1)
    if estado_atual == 'q5':
        return True
    return False

def maquina_questao4_d(fita, estado_atual='q0', i=0):
    if estado_atual == 'q0':
        if len(fita) == i:
            return maquina_questao4_d(fita, 'q10', i + 1)
        if fita[i] == 'a':
            fita[i] = 'A'
            return maquina_questao4_d(fita, 'q1', i + 1)
    if estado_atual == 'q1':
        if fita[i] == 'a' or fita[i] == 'b':
            return maquina_questao4_d(fita, 'q1', i + 1)
        if fita[i] == 'B' or fita[i] == 'c':
            return maquina_questao4_d(fita, 'q3', i - 1)
    if estado_atual == 'q2':
        if fita[i] == 'B' or fita[i] == 'c':
            return maquina_questao4_d(fita, 'q2', i - 1)
        if fita[i] == 'X':
            return maquina_questao4_d(fita, 'q6', i + 1)
    if estado_atual == 'q3':
        if fita[i] == 'b':
            fita[i] = 'B'
            return maquina_questao4_d(fita, 'q4', i - 1)
    if estado_atual == 'q4':
        if fita[i] == 'b':
            return maquina_questao4_d(fita, 'q5', i - 1)
        if fita[i] == 'A':
            return maquina_questao4_d(fita, 'q6', i + 1)
    if estado_atual == 'q5':
        if fita[i] == 'a' or fita[i] == 'b':
            return maquina_questao4_d(fita, 'q5', i - 1)
        if fita[i] == 'A':
            return maquina_questao4_d(fita, 'q0', i + 1)
    if estado_atual == 'q6':
        if fita[i] == 'B':
            fita[i] = 'X'
            return maquina_questao4_d(fita, 'q7', i + 1)
    if estado_atual == 'q7':
        if len(fita) == i:
            return maquina_questao4_d(fita, 'q9', i - 1)
        if fita[i] == 'B' or fita[i] == 'c':
            return maquina_questao4_d(fita, 'q7', i + 1)
        if fita[i] == 'C':
            return maquina_questao4_d(fita, 'q9', i - 1)
    if estado_atual == 'q8':
        if fita[i] == 'c':
            return maquina_questao4_d(fita, 'q2', i - 1)
        if fita[i] == 'X':
            return maquina_questao4_d(fita, 'q10', i - 1)
    if estado_atual == 'q9':
        if fita[i] == 'c':
            fita[i] == 'C'
            return maquina_questao4_d(fita, 'q8', i - 1)
    if estado_atual == 'q10':
        return True
    return False