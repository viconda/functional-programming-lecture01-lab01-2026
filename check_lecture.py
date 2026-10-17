"""Выполнить все примеры лекции и сохранить фактические журналы."""
import ast
import subprocess
import sys
from pathlib import Path

if __name__ == '__main__':
    directory=Path(__file__).resolve().parent/'lecture01'
    scripts=('p31','p32','p33','p34','p35','p36','p37','p4_imp','p4_func','p4_comp','p5','srs1','srs3','srs4')
    logs=directory/'logs'
    logs.mkdir(exist_ok=True)
    total=0
    print('ПРОВЕРКА ВСЕХ ПРОГРАММ ЛЕКЦИИ И СРС')
    for name in scripts:
        source=directory/(name+'.py')
        count=sum(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(source.read_text(encoding='utf-8'))))
        result=subprocess.run([sys.executable,'-X','utf8',str(source)],cwd=directory,capture_output=True,text=True,encoding='utf-8')
        (logs/(name+'.txt')).write_text(result.stdout+result.stderr,encoding='utf-8')
        print(f'{name}.py: assert={count}, код завершения={result.returncode}')
        total+=count
        if result.returncode: print(result.stderr); raise SystemExit(result.returncode)
    print(f'Итого: {len(scripts)} программ, {total} собственных assert.')
    print('СРС1 также выполняет четыре assert вложенного запуска p31.')
    print('Все программы завершились успешно.')
