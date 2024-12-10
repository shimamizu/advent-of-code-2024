#!/usr/bin/env python3

# import standard libraries
from __future__ import annotations
import logging
import sys

# import local libraries
from lib.common import CommonLibrary

# import libraries needing to be pip installed
try:
    from rich.console import Console
except ImportError as import_error:
    logging.warning(f"Import error found: {import_error}")
    sys.exit()
except Exception:
    logging.exception("Hit some other exception during imports")
    sys.exit()

console: Console = Console()

example_data: str = "7 6 4 2 1\n" "1 2 7 8 9\n" "9 7 6 2 1\n" "1 3 2 4 5\n" "8 6 4 4 1\n" "1 3 6 7 9"


def increase_decrease_same(report: list[int], index: int) -> str:
    """Check if increasing or decreasing."""
    index_next = index + 1
    too_high: int = 4
    if abs(report[index] - report[index_next]) >= too_high:
        return "unsafe"
    if report[index] > report[index_next]:
        return "increasing" if abs(report[index] - report[index_next]) < too_high else "unsafe"
    if report[index] < report[index_next]:
        return "decreasing" if abs(report[index] - report[index_next]) < too_high else "unsafe"
    return "unsafe"


def check_if_safe(report: list[int]) -> tuple[str, int]:
    """Check if the report is safe or unsafe."""
    report_length: int = len(report)
    report_loop = report_length - 1
    list_type_start: str = increase_decrease_same(report, 0)
    report_index: int = 1
    if list_type_start == "unsafe":
        return ("UNSAFE", report_index)
    while report_index < report_loop:
        list_type_now = increase_decrease_same(report, report_index)
        if list_type_start != list_type_now or list_type_now == "unsafe":
            return ("UNSAFE", report_index + 1)
        report_index += 1
    return ("SAFE", 0)


def main(input_data: str) -> None:
    """Calculate if levels are safe."""
    master_list: list[str] = [line.strip() for line in input_data.splitlines()]
    report_list = []
    report_list = [list(map(int, report.split())) for report in master_list]
    how_many_safe: int = 0
    unsafe_list = []
    for report in report_list:
        report_safety, report_index = check_if_safe(report)
        if report_safety == "SAFE":
            how_many_safe += 1
        else:
            unsafe_list.append(report)
    console.print(f"[bold]Number of safe reports (Part 1 answer):[/bold] {how_many_safe}")

    for report in unsafe_list:
        for index, _item in enumerate(report):
            copy = report.copy()
            copy.pop(index)
            report_safety, report_index = check_if_safe(copy)
            if report_safety == "SAFE":
                how_many_safe += 1
                break

    console.print(f"[bold]Number of safe reports (Part 2 answer):[/bold] {how_many_safe}")


if __name__ == "__main__":
    my_input_data: str | None = CommonLibrary.get_daily_input(2)
    if my_input_data is not None:
        main(my_input_data)
