# tests/core/test_runner.py
"""
A simple test for run_python_file() in core/runner.py.

What this does:
1. Creates a tiny throwaway Python file that just prints something.
2. Runs it using our run_python_file() function.
3. Checks that the printed text actually showed up.

Run it with:
    pytest tests/core/test_code_runner.py -v
"""
from PyQt6.QtWidgets import QApplication

from core.code_runner import run_python_file


def test_run_python_file_prints_output(tmp_path, capsys):
    # QProcess (used inside run_python_file) needs a QApplication to exist.
    QApplication.instance() or QApplication([])

    # 1. Create a temporary .py file that just prints a message.
    script_path = tmp_path / "hello.py"
    script_path.write_text('print("Hello, World!")')

    # 2. Run it with our function.
    process = run_python_file(str(script_path))

    # 3. Wait for it to finish (give it up to 5 seconds).
    process.waitForFinished(5000)

    # 4. Check that "Hello, World!" was actually printed.
    printed_output = capsys.readouterr().out
    assert "Hello, World!" in printed_output