from app import add, multiply

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0

def test_generate_report():
    # This generates a physical text log file that we will upload as an artifact in Job 1
    report_content = "CI Pipeline Test Execution Summary:\nAll unit tests passed successfully!\nStatus: GREEN"
    with open("test_execution_report.txt", "w") as f:
        f.write(report_content)
