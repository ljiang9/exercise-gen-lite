"""exercise_gen_lite: 英语练习生成（填空/造句/选择），答案确定性。"""
from .gen import fill_blank, multiple_choice, make_sentence, WORD_BANK, SENTENCE_BANK

__all__ = ["fill_blank", "multiple_choice", "make_sentence", "WORD_BANK", "SENTENCE_BANK"]
__version__ = "0.1.0"
