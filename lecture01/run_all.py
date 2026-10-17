"""Запустить все практические фрагменты лекции и СРС."""

import subprocess
import sys
from pathlib import Path

SCRIPTS = (
    "p31.py",
    "p32.py",
    "p33.py",
    "p34.py",
    "p35.py",
    "p36.py",
    "p37.py",
    "p4_imp.py",
    "p4_func.py",
    "p4_comp.py",
    "p5.py",
    "srs1.py",
    "srs3.py",
    "srs4.py",
)

if __name__ == "__main__":
    for script in SCRIPTS:
        print(f"\n=== {script} ===", flush=True)
        subprocess.run(
            [sys.executable, "-X", "utf8", script],
            cwd=Path(__file__).parent,
            check=True,
        )
    print("\nИТОГ: 14 скриптов завершились без ошибок.")
