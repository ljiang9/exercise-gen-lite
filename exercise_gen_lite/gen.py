"""英语练习生成。内置词表与句型，输出题目+确定答案。"""
from __future__ import annotations
from dataclasses import dataclass

WORD_BANK = [
    {"word": "apple", "pos": "n.", "meaning": "苹果"},
    {"word": "run", "pos": "v.", "meaning": "跑"},
    {"word": "happy", "pos": "adj.", "meaning": "开心的"},
    {"word": "book", "pos": "n.", "meaning": "书"},
    {"word": "quickly", "pos": "adv.", "meaning": "快速地"},
]
SENTENCE_BANK = [
    "I like to read a ___ after dinner.",
    "She ___ to school every day.",
    "They felt ___ about the news.",
]


@dataclass
class FillBlank:
    question: str
    answer: str


def fill_blank(index=0):
    idx = index % len(SENTENCE_BANK)
    answers = ["book", "run", "happy"]
    return FillBlank(question=SENTENCE_BANK[idx], answer=answers[idx])


@dataclass
class Choice:
    question: str
    options: list
    answer_index: int


def multiple_choice(index=0):
    idx = index % len(WORD_BANK)
    correct = WORD_BANK[idx]["word"]
    others = [w["word"] for i, w in enumerate(WORD_BANK) if i != idx][:2]
    return Choice(question=f"选择正确的释义：{correct} ({WORD_BANK[idx]['pos']})", options=[correct]+others, answer_index=0)


def make_sentence(index=0):
    idx = index % len(WORD_BANK)
    w = WORD_BANK[idx]
    return {"word": w["word"], "example": f"I ate an {w['word']}.", "meaning": w["meaning"]}
