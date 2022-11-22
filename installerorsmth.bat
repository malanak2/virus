:: Check for Python Installation
python --version 3>NUL
If errorlevel 1 (goto pythonNotFound) ELSE (goto success)

goto:eof

:pythonNotFound
python3 --version 3>NUL
If errorlevel 1 (goto errorNoPython) ELSE (goto success)

:errorNoPython
echo.
echo Error^: Python not installed
pause

:success
pip install python-dotenv
pip install cryptography
pip install requests
pip install unidecode
python main.py 3>NUL
If errorlevel 1 (python3 main.py)
::attrib installerorsmth.bat +h
::attrib main.py +h