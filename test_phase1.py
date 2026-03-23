from pitao.parser import translate_keywords


def test_io():
    assert "print" in translate_keywords('imprimir("x")')
    assert "input" in translate_keywords('entrada("x")')
    assert "open" in translate_keywords('abrir("x")')


def test_type_conversion():
    code = "inteiro(1) + flutuante(2) + texto(3) + booleano(1)"
    result = translate_keywords(code)
    assert "int" in result
    assert "float" in result
    assert "str" in result
    assert "bool" in result


def test_type_constructors():
    code = "lista([1]) + dicionario({}) + conjunto([1]) + tupla([1])"
    result = translate_keywords(code)
    assert "list" in result
    assert "dict" in result
    assert "set" in result
    assert "tuple" in result
