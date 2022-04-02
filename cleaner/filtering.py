import re
from typing import List


def filter_text(text: str) -> str:
    for filter in FILTERS:
        text = filter(text)

    return text


class Filter:
    def __call__(self, text: str) -> str:
        raise NotImplementedError


def get_filters() -> List[Filter]:
    return [
        PatternFilter('&lt;.*&gt;'),
        PatternFilter('&apos;'),
        PatternFilter('\%[a-z_]+\%'),
        SomeComplexFilter(),
    ]


class PatternFilter(Filter):
    def __init__(self, pattern: str):
        self.pattern = pattern

    def __call__(self, text):
        return re.sub(self.pattern, '', text)


class SomeComplexFilter(Filter):
    def __call__(self, text):
        return text


FILTERS = get_filters()
