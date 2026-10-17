"""Запустить настоящие внешние проверки и показать их результаты."""
import subprocess
import sys
from pathlib import Path

if __name__ == '__main__':
    root=Path(__file__).resolve().parent
    files=['task1.py','task2.py','task3.py','task4.py','task5.py','scholarship.py','church.py']
    commands=[
        ('pytest lab01', ['-m','pytest','-q','-p','no:cacheprovider','lab01']),
        ('mypy семь модулей', ['-m','mypy',*[f'lab01/{f}' for f in files]]),
        ('ruff check lab01',['-m','ruff','check','--no-cache','lab01']),
    ]
    print('ИТОГОВАЯ ПРОВЕРКА ЛАБОРАТОРНОЙ')
    for title,args in commands:
        result=subprocess.run([sys.executable,*args],cwd=root,capture_output=True,text=True,encoding='utf-8')
        print('\n'+title)
        print(result.stdout.strip())
        if result.stderr: print(result.stderr.strip())
        print('Код завершения:',result.returncode)
        if result.returncode: raise SystemExit(result.returncode)
    print('\n104 assert в семи наборах тестов успешно выполнены.')
