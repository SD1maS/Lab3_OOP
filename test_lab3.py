import unittest
from lab3 import Clothing, ClothingManager

class TestClothingManager(unittest.TestCase):

    def setUp(self):
        self.c1 = Clothing("Футболка", "M", 500.0, "Білий", 0.15)
        self.c2 = Clothing("Шорти", "M", 500.0, "Сірий", 0.20)
        self.c3 = Clothing("Джинси", "L", 1200.0, "Синій", 0.80)
        self.c4 = Clothing("Куртка", "XL", 1200.0, "Чорний", 1.50)
        self.c5 = Clothing("Шкарпетки", "S", 50.0, "Чорний", 0.05)

        self.clothes = [self.c1, self.c2, self.c3, self.c4, self.c5]

    def test_sort_clothing(self):
        # Очікуваний результат: 
        # Шкарпетки, 50.0, 0.05
        # Шорти 300.0, 0.20
        # Футболка 300.0, 0.15
        # Куртка 1200.0, 1.50
        # Джинси 1200.0, 0.80
        expected_order = [self.c5, self.c2, self.c1, self.c4, self.c3]
        sorted_clothes = ClothingManager.sort_clothing(self.clothes)
        self.assertEqual(sorted_clothes, expected_order)

    def test_find_same_success(self):
        target = Clothing("Джинси", "L", 1200.0, "Синій", 0.80)
        index = ClothingManager.find_same(self.clothes, target)
        self.assertEqual(index, 2)

    def test_find_same_not_found(self):
        target = Clothing("Кепка", "M", 200.0, "Блакитний", 0.10)
        index = ClothingManager.find_same(self.clothes, target)
        self.assertEqual(index, -1)

if __name__ == '__main__':
    unittest.main()