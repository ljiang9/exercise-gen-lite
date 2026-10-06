import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from exercise_gen_lite.gen import fill_blank, multiple_choice, make_sentence, WORD_BANK


class TestExerciseGen(unittest.TestCase):
    def test_fill_blank_deterministic(self):
        a = fill_blank(0); b = fill_blank(0)
        self.assertEqual(a.answer, "book"); self.assertEqual(a.question, b.question)
    def test_fill_blank_cycle(self):
        self.assertEqual(fill_blank(3).answer, "book")
    def test_mc_answer(self):
        c = multiple_choice(0)
        self.assertEqual(c.answer_index, 0); self.assertEqual(c.options[0], "apple")
    def test_mc_cycle(self):
        c = multiple_choice(5)
        self.assertIn(c.options[c.answer_index], {w["word"] for w in WORD_BANK})
    def test_make_sentence(self):
        s = make_sentence(0)
        self.assertEqual(s["word"], "apple"); self.assertIn("apple", s["example"])


if __name__ == "__main__": unittest.main()
