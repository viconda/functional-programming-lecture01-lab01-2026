"""Показать фактически используемое окружение учебного проекта."""
import importlib.metadata
import subprocess
import sys
from pathlib import Path

if __name__ == '__main__':
    root=Path(__file__).resolve().parent
    print('ПОДГОТОВКА ОКРУЖЕНИЯ')
    print('Python:', sys.version.split()[0])
    print('Виртуальное окружение активно:', sys.prefix != sys.base_prefix)
    print('Проект:', root.name)
    print('Папка:', root.parent)
    print('Каталог lab01 существует:', (root/'lab01').is_dir())
    for name in ('ruff','mypy','pytest'):
        print(name+':', importlib.metadata.version(name))
    git=Path(r'C:\Users\shvac\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\git\cmd\git.exe')
    result=subprocess.run([str(git),'--version'],capture_output=True,text=True,check=True)
    print(result.stdout.strip())
    result=subprocess.run([str(git),'rev-list','--count','HEAD'],cwd=root,capture_output=True,text=True,check=True)
    print('Коммитов в учебном репозитории:',result.stdout.strip())
