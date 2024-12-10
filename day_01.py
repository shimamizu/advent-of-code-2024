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

example_data: str = "3   4\n" "4   3\n" "2   5\n" "1   3\n" "3   9\n" "3   3\n"


def main(input_data: str) -> None:
    """Calculate the total distance between lists."""
    master_list: list[str] = [line.strip() for line in input_data.splitlines()]
    left_list: list[int] = []
    right_list: list[int] = []
    for line in master_list:
        left_list.append(int(line.split("   ")[0]))
        right_list.append(int(line.split("   ")[1]))
    left_list_sorted: list[int] = sorted(left_list)
    right_list_sorted: list[int] = sorted(right_list)

    list_length = len(master_list)
    console.print(f"[bold]Length of input list:[/bold] {list_length:,}", highlight=False)
    left_list_sum: int = sum(left_list)
    right_list_sum: int = sum(right_list)
    console.print(f"[bold]Left list sum:[/bold] {left_list_sum:,}", highlight=False)
    console.print(f"[bold]Right list sum:[/bold] {right_list_sum:,}", highlight=False)
    list_sum_difference = abs(left_list_sum - right_list_sum)
    console.print(f"[bold]Total difference of list sums:[/bold] {list_sum_difference:,}", highlight=False)

    # Calculate the answer to Part 1:
    list_index: int = 0
    distance_list: list[int] = []
    while list_index < list_length:
        distance_list.append(abs(left_list_sorted[list_index] - right_list_sorted[list_index]))
        list_index += 1
    total_distance = sum(distance_list)
    console.print(f"[bold]Total distance between lists:[/bold] {total_distance}")

    # Calculate the answer to Part 2:
    similarity_list: list[int] = []
    for loc_id in left_list:
        occurence_count: int = right_list.count(loc_id)
        similarity_score: int = loc_id * occurence_count
        similarity_list.append(similarity_score)
    similarity_sum = sum(similarity_list)
    console.print(f"[bold]Total similarity score sum:[/bold] {similarity_sum}")


if __name__ == "__main__":
    my_input_data: str | None = CommonLibrary.get_daily_input(1)
    if my_input_data is not None:
        main(my_input_data)
