import unittest
from slownie2 import slownie

class TestSlownie(unittest.TestCase):
    def setUp(self):
        self.slownie = slownie

    def test_slownie_type(self):
        self.assertRaises(TypeError, self.slownie, "NOT INT")

    def test_slownie_range(self):
        self.assertRaises(ValueError, self.slownie, -1)
        self.assertRaises(ValueError, self.slownie, 1001)

    def test_slownie_0_10(self):
        self.assertEqual("zero", self.slownie(0))
        self.assertEqual("jeden", self.slownie(1))
        self.assertEqual("dwa", self.slownie(2))
        self.assertEqual("trzy", self.slownie(3))
        self.assertEqual("cztery", self.slownie(4))
        self.assertEqual("pięć", self.slownie(5))
        self.assertEqual("sześć", self.slownie(6))
        self.assertEqual("siedem", self.slownie(7))
        self.assertEqual("osiem", self.slownie(8))
        self.assertEqual("dziewięć", self.slownie(9))
        self.assertEqual("dziesięć", self.slownie(10))

    def test_slownie_10_19(self):
        self.assertEqual("dziesięć", self.slownie(10))
        self.assertEqual("jedenaście", self.slownie(11))
        self.assertEqual("dwanaście", self.slownie(12))
        self.assertEqual("trzynaście", self.slownie(13))
        self.assertEqual("czternaście", self.slownie(14))
        self.assertEqual("piętnaście", self.slownie(15))
        self.assertEqual("szesnaście", self.slownie(16))
        self.assertEqual("siedemnaście", self.slownie(17))
        self.assertEqual("osiemnaście", self.slownie(18))
        self.assertEqual("dziewiętnaście", self.slownie(19))

    def test_slownie_10_rounded(self):
        self.assertEqual("dziesięć", self.slownie(10))
        self.assertEqual("dwadzieścia", self.slownie(20))
        self.assertEqual("trzydzieści", self.slownie(30))
        self.assertEqual("czterdzieści", self.slownie(40))
        self.assertEqual("pięćdziesiąt", self.slownie(50))
        self.assertEqual("sześćdziesiąt", self.slownie(60))
        self.assertEqual("siedemdziesiąt", self.slownie(70))
        self.assertEqual("osiemdziesiąt", self.slownie(80))
        self.assertEqual("dziewięćdziesiąt", self.slownie(90))

    def test_slownie_10_not_rounded(self):
        self.assertEqual("dwadzieścia jeden", self.slownie(21))
        self.assertEqual("trzydzieści trzy", self.slownie(33))
        self.assertEqual("czterdzieści pięć", self.slownie(45))
        self.assertEqual("sześćdziesiąt siedem", self.slownie(67))
        self.assertEqual("siedemdziesiąt jeden", self.slownie(71))
        self.assertEqual("siedemdziesiąt osiem", self.slownie(78))
        self.assertEqual("osiemdziesiąt osiem", self.slownie(88))
        self.assertEqual("dziewięćdziesiąt jeden", self.slownie(91))
        self.assertEqual("dziewięćdziesiąt cztery", self.slownie(94))

    def test_slownie_100_rounded(self):
        self.assertEqual("sto", self.slownie(100))
        self.assertEqual("dwieście", self.slownie(200))
        self.assertEqual("trzysta", self.slownie(300))
        self.assertEqual("czterysta", self.slownie(400))
        self.assertEqual("pięćset", self.slownie(500))
        self.assertEqual("sześćset", self.slownie(600))
        self.assertEqual("siedemset", self.slownie(700))
        self.assertEqual("osiemset", self.slownie(800))
        self.assertEqual("dziewięćset", self.slownie(900))

    def test_slownie_100_not_rounded(self):
        self.assertEqual("sto jeden", self.slownie(101))
        self.assertEqual("dwieście trzydzieści trzy", self.slownie(233))
        self.assertEqual("trzysta dziewięć", self.slownie(309))
        self.assertEqual("czterysta dwadzieścia trzy", self.slownie(423))
        self.assertEqual("pięćset czterdzieści pięć", self.slownie(545))
        self.assertEqual("sześćset siedem", self.slownie(607))
        self.assertEqual("siedemset siedemdziesiąt dwa", self.slownie(772))
        self.assertEqual("osiemset pięć", self.slownie(805))
        self.assertEqual("dziewięćset dwadzieścia dwa", self.slownie(922))


if __name__ == '__main__':
    unittest.main()
