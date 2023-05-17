@echo off
"C:\Users\Stelios\Anaconda3\python.exe" "C:\Users\Stelios\Desktop\CODE_TEST\02_Python\api\api_server.py"
@echo off
cd ".\Desktop\CODE_TEST\02_Python\api\" "python.exe  pytest -v --html=test_suite_report.htl"

pause