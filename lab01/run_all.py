"""Служебный запуск всех решений с сохранением фактических журналов."""

import ast
import json
import subprocess
import sys
from pathlib import Path


def main() -> None:
    """Запустить восемь независимых программ и записать результаты рядом с кодом."""
    directory = Path(__file__).resolve().parent
    logs = directory / "logs"
    logs.mkdir(exist_ok=True)
    results = []
    for name in (
        "task1",
        "task2",
        "task3",
        "task4",
        "task5",
        "scholarship_original",
        "scholarship",
        "church",
    ):
        source = directory / f"{name}.py"
        assert_count = sum(
            isinstance(node, ast.Assert)
            for node in ast.walk(ast.parse(source.read_text(encoding="utf-8")))
        )
        result = subprocess.run(
            [sys.executable, "-X", "utf8", str(source)],
            check=False,
            cwd=directory,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        (logs / f"{name}.txt").write_text(
            result.stdout + result.stderr, encoding="utf-8"
        )
        print(f"{name}.py: assert={assert_count}, exit={result.returncode}")
        print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, end="")
        results.append(
            {
                "module": name,
                "asserts": assert_count,
                "exit_code": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
            }
        )
    notes = {
        "python": sys.version,
        "command": "python -X utf8 run_all.py",
        "total_asserts": sum(item["asserts"] for item in results),
        "all_passed": all(item["exit_code"] == 0 for item in results),
        "results": results,
        "limits": [
            "impure_examples.py сохраняет исходный код преподавателя буквально.",
            "scholarship_original.py воспроизводит исходный нечистый calc_scholarship: чтение BASE, изменение student и log, печать. Его демонстрация добавлена отдельно, семь наборов тестов и104 assert чистых решений не изменены.",
            "Шкала task4 общая SU; конкретный силлабус CSE6742 не предоставлен.",
            "Данные студентов в task4 учебные, а не реальные ведомости.",
            "Пустой заказ даёт доставку 1500 согласно логике исходного кода.",
            "from_int принимает целые неотрицательные числа; большие значения ограничены рекурсией.",
            "Чистота функций высшего порядка зависит от чистоты переданных функций.",
            "check_purity выполняет проверяемый код и допускает его побочные эффекты.",
            "Heuristic bool deterministic означает совпадение только наблюдённых запусков.",
        ],
    }
    (directory / "lab_code_notes.json").write_text(
        json.dumps(notes, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(
        f"Всего assert: {notes['total_asserts']}; все программы успешны: {notes['all_passed']}"
    )
    if not notes["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
