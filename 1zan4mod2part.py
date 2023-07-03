#Проверяется входная строка с перевёрнутой
def pallindrom(stroka):
    if stroka[::-1] == stroka:
        return True
    else:
        return False
