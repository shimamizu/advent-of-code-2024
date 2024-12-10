# import standard libraries
from __future__ import annotations
import logging
import os
import sys

# import additional libraries
try:
    import requests
except ImportError as import_error:
    logging.warning(f"Import error found: {import_error}")
    sys.exit()
except Exception:
    logging.exception("Hit some other exception during imports")
    sys.exit()


class CommonLibrary:
    """Common library functions for Advent of Code 2024."""

    @staticmethod
    def get_daily_input(day_number: int) -> str | None:
        """Get the daily input from Advent of Code 2024."""
        url = f"https://adventofcode.com/2024/day/{day_number}/input"
        cookies = {"session": os.environ["ADVENT_OF_CODE_SESSION"]}
        response = requests.get(url, cookies=cookies, timeout=10)
        successful_status: int = 200
        if response.status_code == successful_status:
            page_content = response.text
        else:
            print(f"Failed to fetch page. Status code: {response.status_code}")
            page_content = None
            sys.exit()
        return page_content
