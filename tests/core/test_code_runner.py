"""
A simple test for run_python_file() in core/runner.py.

Run it with:
    pytest tests/core/test_code_runner.py -v
"""
from PyQt6.QtWidgets import QApplication
from core.code_runner import run_python_file


def test_run_python_file(tmp_path, capsys):
    # QProcess (used inside run_python_file) needs a QApplication to exist.
    QApplication.instance() or QApplication([])

    # Create a temporary .py file that just prints a message.
    temp_script_path = tmp_path / "hello.py"
    temp_script_path.write_text('print("Hello, World!")')

    # Run it with our function.
    process = run_python_file(str(temp_script_path))

    # Wait for it to finish (give it up to 5 seconds).
    process.waitForFinished(5000)

    # the output of the process
    printed_output = capsys.readouterr().out
    # Check that "Hello, World!" was actually printed.
    assert "Hello, World!" in printed_output