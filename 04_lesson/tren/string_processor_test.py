import pytest
from string_processor import StringProcessor

@pytest.mark.parametrize("input, expected",
    [
    ("kadia","Kadia."),
    ("кадия стоит","Кадия стоит."),
    ("Кадия", "Кадия.")
    ]
)
def test_process_positive(input, expected):
    processor = StringProcessor()
    assert processor.process(input) == expected


@pytest.mark.parametrize(
    "input_text, expected_output",
    [("", "."), ("    ", "    .")],
)
def test_process_negative(input_text, expected_output):
    processor = StringProcessor()
    assert processor.process(input_text) == expected_output