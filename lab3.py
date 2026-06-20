class Clothing:
    def __init__(self, name: str, size: str, price: float, color: str, weight: float):
        self.name = name
        self.size = size
        self.price = price
        self.color = color
        self.weight = weight
        
    def __eq__(self, other):
        if not isinstance(other, Clothing):
            return False
        return (self.name == other.name and
                self.size == other.size and
                self.price == other.price and
                self.color == other.color and
                self.weight == other.weight)
    
    def __str__(self):
        return f"Назва: {self.name}, Розмір: {self.size}, Ціна: {self.price} грн., Колір: {self.color}, Вага: {self.weight})"


class ClothingManager:
    @staticmethod
    def sort_clothing(clothes: list[Clothing]) -> list[Clothing]:
        return sorted(clothes, key=lambda c: (c.price, -c.weight))

    @staticmethod
    def find_same(clothes: list[Clothing], target: Clothing) -> int:
        for i, item in enumerate(clothes):
            if item == target:
                return i
        return -1
    

def main():
    clothes_array = [
        Clothing("Футболка", "M", 600.0, "Білий", 0.15),
        Clothing("Шорти", "M", 400.0, "Сірий", 0.20),
        Clothing("Джинси", "L", 1200.0, "Синій", 0.80),
        Clothing("Куртка", "XL", 1200.0, "Чорний", 1.50),
        Clothing("Шкарпетки", "S", 50.0, "Чорний", 0.05)]
    
    target_clothing = Clothing("Джинси", "L", 1200.0, "Синій", 0.80)

    print("\033[1mПочатковий масив:\033[0m")
    for c in clothes_array:
        print(c)
        
    sorted_clothes = ClothingManager.sort_clothing(clothes_array)

    print("\n\033[1mВідсортований масив (Ціна ↑, Вага ↓):\033[0m")
    for c in sorted_clothes:
        print(c)

    print("\n\033[1mПошук заданого об'єкта:\033[0m")
    print(f"Шукаємо об'єкт: {target_clothing}")

    index = ClothingManager.find_same(sorted_clothes, target_clothing)
    
    if index != -1:
        print(f"Об'єкт знайдено. Індекс у відсортованому масиві: {index}")
    else:
        print("Об'єкт не знайдено.")

if __name__ == "__main__":
    main()