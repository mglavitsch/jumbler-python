import unittest
from jumblepkg.jumble import Jumbler


class TestJumbler(unittest.TestCase):

    def test_indices(self):
        # print(sys.getdefaultencoding())
        jumbler = Jumbler("          ")
        indices = jumbler.get_indices()
        self.assertEqual(indices, [])

        jumbler.text = "Zaphod Beeblebrox"
        indices = jumbler.get_indices()
        self.assertEqual(indices, [[0, 5], [7, 16]])

        jumbler.text = "   Zaphod __äöü___ $ Beeble123brox !?+ "
        indices = jumbler.get_indices()
        self.assertEqual(indices, [[3, 8], [12, 14], [21, 26], [30, 33]])

        jumbler.text = "Arthur Dent\nFord Prefect\nTricia McMillan\nZaphod Beeblebrox"
        indices = jumbler.get_indices()
        self.assertEqual(indices, [[0, 5], [7, 10], [12, 15], [17, 23], [
                         25, 30], [32, 39], [41, 46], [48, 57]])

    def test_jumble(self):
        jumbler = Jumbler("          ")
        jumbled_text = jumbler.get_jumbled_text(True, 1000)
        self.assertEqual(jumbled_text, "          ")

        jumbler.text = "Zaphod Beeblebrox"
        jumbled_text = jumbler.get_jumbled_text(True, 1000)
        self.assertEqual(jumbled_text, "Zohapd Bbeeboelrx")

        jumbler.text = "   Zaphod __äöü___ $ Beeble123brox !?+ "
        jumbled_text = jumbler.get_jumbled_text(True, 1000)
        self.assertEqual(
            jumbled_text, "   Zohapd __äöü___ $ Bbelee123borx !?+ ")

        jumbler.text = "Arthur Dent\nFord Prefect\nTricia McMillan\nZaphod Beeblebrox"
        jumbled_text = jumbler.get_jumbled_text(True, 1000)
        self.assertEqual(
            jumbled_text, "Auhrtr Dnet\nFrod Pcereft\nTciira MaiMlcln\nZoahpd Blerbboeex")


if __name__ == '__main__':
    unittest.main()
