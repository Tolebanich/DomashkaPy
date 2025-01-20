# int - 19
# float - 2.6
# str - "Test"
# dict - {}
# list - []
# class - anyclass

def do_it(param_1 : int, param_2 : int, param_3 : int):
    """
        # Эта функция берёт первые два параметра,складывает их и делит на 3й.
        
        # Результат печатается в консоль.
        
        Параметры должны быть числовыми.
    """
    result = (param_1 + param_2) * param_3
    return result

do_it(10,20,30)
