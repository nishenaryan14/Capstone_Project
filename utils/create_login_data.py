import openpyxl, os

def create_excel_data():
    os.makedirs("test_data", exist_ok=True)

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "LoginTests"

    headers = ["TestCaseID", "Username", "Password", "ExpectedResult"]
    ws.append(headers)

    rows = [
        ("TC001", "standard_user", "secret_sauce", "Success"),
        ("TC002", "locked_out_user", "secret_sauce", "Error"),
        ("TC003", "problem_user", "secret_sauce", "Success"),
        ("TC004", "performance_glitch_user", "secret_sauce", "Success"),
        ("TC005", "wrong_user", "wrong_pass", "Error"),
        ("TC006", "", "secret_sauce", "Error"),
        ("TC007", "standard_user", "", "Error"),
    ]
    for r in rows:
        ws.append(r)

    wb.save("test_data/login_data.xlsx")
    print("✅ Excel created → test_data/login_data.xlsx")


if __name__ == "__main__":
    create_excel_data()