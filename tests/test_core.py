from hwconvert.core import convert_file


def test_txt_to_txt(tmp_path):
    file = tmp_path / "a.txt"
    file.write_text("hello")

    result = convert_file(str(file), "txt")
    assert result == "hello"