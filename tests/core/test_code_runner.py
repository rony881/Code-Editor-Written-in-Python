"""
A simple test for run_python_file() in core/runner.py.

Run it with:
    pytest tests/core/test_code_runner.py -v
"""
from core.code_runner import run_python_file


def test_run_python_file(tmp_path, capsys):
    temp_script_path = tmp_path / "hello.py"
    temp_script_path.write_text('print("Hello, World!")')

    process = run_python_file(str(temp_script_path))
    process.waitForFinished(5000)
    printed_output = capsys.readouterr().out

    assert "Hello, World!" in printed_output