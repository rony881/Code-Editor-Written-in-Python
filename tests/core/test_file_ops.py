from core.file_ops import read_file


def test_read_file(tmp_path):
    expected_content = (
        "Content:\n"
        "Hello, world!\n"
        "This is a test file.\n\n"
        "File name:\n"
        "test.txt"
    )

    test_file = tmp_path / "test.txt"
    test_file.write_text(expected_content)

    content, file_name = read_file(str(test_file))

    assert content == expected_content, "Content does not match"
    assert file_name == "test.txt", "File name does not match"
