import pytest
from string_utils import StringUtils


#1 позитивные проверки на заглавные символы
@pytest.mark.parametrize("input_string, expected_output",
    [
    ("кадия", "Кадия"),
    ("istvaan", "Istvaan"),
    ("чМаффКи", "Чмаффки"),
    ("истваан 5", "Истваан 5")
    ]
    )
def test_capitalize_positive(input_string, expected_output):
    stringU = StringUtils()
    assert stringU.capitilize(input_string) == expected_output


#2 негативные проверки на заглавные символы
@pytest.mark.parametrize("input_string, expected_output",
    [
    ("     ", "     "),
    (None, None),
    ("43132", "43132")
    ]
    )
@pytest.mark.xfail #Ошибка высвечивается на None.Вынести эту проверку отдельно или можно оставить тут xfail? Ибо остальные прошли и это видно.
def test_capitalize_negative(input_string, expected_output):
    stringU = StringUtils()
    assert stringU.capitilize(input_string) == expected_output


@pytest.mark.parametrize("input_string, expected_output",
    [
    (None, None)
    ]
    )
# @pytest.mark.xfail #Вынес отдельно.Так нагляднее,но вопрос остался.
def test_capitalize_negative(input_string, expected_output):
    stringU = StringUtils()
    import pytest
    with pytest.raises(AttributeError):
        stringU.capitilize(input_string) == expected_output


#3 Позитивные проверки удаления пробелов
@pytest.mark.parametrize("input,expected_output",
    [
        ("  Император","Император"),
        ("  1234", "1234"),
        ("  Слава Императору человечества!", "Слава Императору человечества!")
    ]
    )
def test_trim_positive(input, expected_output):
    trim = StringUtils()
    assert trim.trim(input) == expected_output


#4 Негативные проверки удаления пробелов
@pytest.mark.parametrize("input,expected_output",
    [
        ("  ",""), #Является ли позитивной или негативной проверкой?т.к. пробелы удаляет,но там просто пустое поле,получается
        ("", ""),
        (None, None)
    ]
    )
@pytest.mark.xfail
def test_trim_negative(input, expected_output):
    trim = StringUtils()
    assert trim.trim(input) == expected_output


#5 Позитивные проверки to_list
@pytest.mark.parametrize("list, delimetr, expected_output",
    [
        ("Кадия,Земля,Марс", ",", ["Кадия", "Земля", "Марс"]),
        ("1,2,3,4,5", ",",["1","2","3","4","5"]),
        ("Ересь-не-пройдёт", "-", ["Ересь", "не", "пройдёт"]),
        ("Магнус:не:предавал", ":", ["Магнус", "не", "предавал"])
    ]
    )
def test_to_list_positive(list, delimetr, expected_output):
    string = StringUtils()
    assert string.to_list(list, delimetr) == expected_output

#6 Негативные проверки to_list
@pytest.mark.parametrize("list, delimetr, expected_output",
    [
        (["Кадия", "Земля", "Марс"], ",", "Кадия,Земля,Марс"),
        ("", ",",[]), #Является ли негативной?по идее программа должна вернуть ошибку что всё пусто и плохо,правда в документации этого нет,но всё же.
        (None, ",", [None])
    ]
    )
@pytest.mark.xfail
def test_to_list_negattive(list, delimetr, expected_output):
    string = StringUtils()
    assert string.to_list(list, delimetr) == expected_output

#7 Позитивные проверки contains
@pytest.mark.parametrize("word, symbol,exp",
    [
        ("Кулаки", "а", True ),
        ("Император", "и", True),  #дефект
        ("Emperor", "e", True),
        ("Арранар", "ц", False)
    ]
    )
def test_contains(word, symbol, exp):
    string = StringUtils()
    assert string.contains(word,symbol) == exp


#8 Негативные проверки contains
@pytest.mark.parametrize("word, symbol,exp",
    [
        ("", "а", False),
        ("Император", "", False), #Дефект
        (None, None, False),
        ("    ", " ", True) #Является ли это дефектом?Пробел символ,как бы,но вряд ли так должно отрабатывать.
    ]
    )
@pytest.mark.xfail
def test_contains(word, symbol, exp):
    string = StringUtils()
    assert string.contains(word,symbol) == exp

# #9 Позитивные проверки delete_symbol
@pytest.mark.parametrize("word,symbol,res",
    [
        ("Еретик","Еретик",""),
        ("Хер майор","Хер", " майор"),
        ("abdomination","ab","domination"),
        ("1234","1","234")
    ]
    )
def test_delete_symbol_positive(word,symbol,res):
    string = StringUtils()
    assert string.delete_symbol(word, symbol) == res

#10 Негативные проверки delete_symbol
@pytest.mark.parametrize("word,symbol,res",
    [
        (1234,1,234), #ожидается ошибка.Но не знаю как красиво оформить
        ("","","")
    ]
    )
@pytest.mark.xfail
def test_delete_symbol_negative(word,symbol,res):
    string = StringUtils()
    assert string.delete_symbol(word, symbol) == res

#11 Позитивные проверки starts_with
@pytest.mark.parametrize("word,start, TF",
    [
        ("Кадия", "К", True),
        ("Emperor", "e", True), #дефект
        ("Heresy", "e", False)
    ]
    )
@pytest.mark.xfail
def test_starts_with_positive(word,start,TF):
    string = StringUtils()
    assert string.starts_with(word, start) == TF

#12 Негативные проверки starts_with
@pytest.mark.parametrize("word,start, TF",
    [
        ("Истваан", "А", True),
        ("Gun", "e", True),
        ("", "", False)
    ]
    )
@pytest.mark.xfail
def test_starts_with_negative(word,start,TF):
    string = StringUtils()
    assert string.starts_with(word, start) == TF

#13 Позитивные проверки end_with
@pytest.mark.parametrize("word, end, TF",
    [
        ("Кадия", "я", True),
        ("Emperor", "r", True),
        ("Heresy", "e", False)
    ]
    )
def test_end_with_positive(word,end,TF):
    string = StringUtils()
    assert string.end_with(word,end) == TF

#14 Негативные проверки end_with
@pytest.mark.parametrize("word,start, TF",
    [
        ("Истваан", "b", True),
        ("Gun", "j", True),
        ("", "", False)
    ]
    )
@pytest.mark.xfail
def test_starts_with_negative(word,start,TF):
    string = StringUtils()
    assert string.starts_with(word, start) == TF

#15 Позитивные проверки is_empty
@pytest.mark.parametrize("field, TF",
    [
        ("",True),
        ("   ", True),
        ("For the Emperor!", False)
    ]
    )
def test_is_empty_positive(field,TF):
    string = StringUtils()
    assert string.is_empty(field) == TF

#16 Негативные проверки is_empty
@pytest.mark.parametrize("field, TF",
    [
        ("1234",False),
        (1234, False),
        ("______!@#$%____", False)
    ]
    )
@pytest.mark.xfail
def test_is_empty_negativee(field,TF):
    string = StringUtils()
    assert string.is_empty(field) == TF


#17 Позитивные проверки list_to_string
@pytest.mark.parametrize("list, delimetr, expected_output",
    [
        (["Кадия", "Земля", "Марс"], ",", "Кадия,Земля,Марс"),
        (["1","2","3","4","5"], ",","1,2,3,4,5"),
        (["Ересь", "не", "пройдёт"], "-", "Ересь-не-пройдёт"),
        (["Магнус", "не", "предавал"], ":", "Магнус:не:предавал")
    ]
    )
def test_list_to_string_positive(list, delimetr, expected_output):
    string = StringUtils()
    assert string.list_to_string(list, delimetr) == expected_output


#18 Негативные проверки list_to_string
@pytest.mark.parametrize("list, delimetr, expected_output",
    [
        ("Кадия,Земля,Марс", ",", ["Кадия", "Земля", "Марс"]),
        (None, ",", [None])
    ]
    )
@pytest.mark.xfail
def test_lits_to_string_negattive(list, delimetr, expected_output):
    string = StringUtils()
    assert string.list_to_string(list, delimetr) == expected_output