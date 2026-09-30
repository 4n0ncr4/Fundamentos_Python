def es_eficiente(km = 20,lt = 2): # 1 False
    rendimiento = km / lt
    if (rendimiento >= 15):
        return True
    
    return False

print(es_eficiente())