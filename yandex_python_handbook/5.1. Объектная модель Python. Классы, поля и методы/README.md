# Ответы и решения задач из хэндбука Яндекс «Основы Python», параграф 5.1

### 5.1. Объектная модель Python. Классы, поля и методы

A. Классная точка
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

B. Классная точка 2.0
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def length(self, point):
        distance = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return round(distance, 2)
```

C. Не нажимай красную кнопку!
```python
class RedButton:
    
    def __init__(self):
        self.counter = 0
    
    def click(self):
        self.counter += 1
        print("Тревога!")
    
    def count(self):
        return self.counter
```

D. Работа не волк
```python
class Programmer:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.rise_counter = 0
        self.salary = 0
        self.time = 0

    def info(self):
        return f"{self.name} {self.time}ч. {self.salary}тгр."
    
    def rise(self):
        if self.position == "Junior":
            self.position = "Middle"
        elif self.position == "Middle":
            self.position = "Senior"
        elif self.position == "Senior":
            self.rise_counter += 1
    
    def work(self, time):
        salaries = {"Junior": 10, "Middle": 15, "Senior": 20}
        self.time += time
        self.salary += time * (salaries[self.position] + self.rise_counter)
```

E. Классный прямоугольник
```python
class Rectangle:
    def __init__(self, corner, opposite_corner):
        self.width = abs(corner[0] - opposite_corner[0])
        self.height = abs(corner[1] - opposite_corner[1])
    
    def area(self):
        result = self.width * self.height
        return round(result, 2)
    
    def perimeter(self):
        result = (self.width + self.height) * 2
        return round(result, 2)
```

F. Классный прямоугольник 2.0
```python
class Rectangle:
    def __init__(self, corner, opposite_corner):
        self.x = min(corner[0], opposite_corner[0]) 
        self.y = max(corner[1], opposite_corner[1])
        self.width = abs(corner[0] - opposite_corner[0])
        self.height = abs(corner[1] - opposite_corner[1])
    
    def area(self):
        result = self.width * self.height
        return round(result, 2)
    
    def perimeter(self):
        result = (self.width + self.height) * 2
        return round(result, 2)

    def get_pos(self):
        return round(self.x, 2), round(self.y, 2)
    
    def get_size(self):
        return round(self.width, 2), round(self.height, 2)
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def resize(self, width, height):
        self.width, self.height = width, height
        self.width, self.height = width, height
```

G. Классный прямоугольник 3.0

#### Общая стратегия и примеры:

1. Определение точки вращения:

    Прежде всего, определите точку, относительно которой вы будете вращать прямоугольник. Обычно это центр прямоугольника, но может быть и любая другая точка.

2. Преобразование координат:

    Для каждого угла прямоугольника выполните следующие шаги:

    a. Перенесите координаты так, чтобы точка вращения была в начале координат (0, 0). Если точка вращения имеет координаты (cx, cy), то для угла (x, y) новые координаты (x’, y’) будут:

    ```
    x' = x - cx
    y' = y - cy
    ```

    b. Выполните поворот на 90 градусов по часовой стрелке. Формулы для поворота на 90 градусов по часовой стрелке:

    ```
    x_rotated = y'
    y_rotated = -x'
    ```

    c. Верните координаты обратно, чтобы точка вращения вернулась в исходное положение.

    ```
    x_final = x_rotated + cx
    y_final = y_rotated + cy
    ```

#### Базовые знания о повороте:

В общем случае, поворот точки (x, y) на угол θ (тета) против часовой стрелки вокруг начала координат (0, 0) выражается следующими формулами:

$$x' = x * cos(θ) - y * sin(θ)$$
$$y' = x * sin(θ) + y * cos(θ)$$

где $(x’, y’)$ - координаты повернутой точки.

1. Поворот на 90 градусов против часовой стрелки:

    При повороте на 90 градусов против часовой стрелки (θ = π/2 радиан или 90°):

    $$cos(π/2) = 0$$
    $$sin(π/2) = 1$$

    Подставляя эти значения в общие формулы поворота, получаем:

    $$x' = x * 0 - y * 1  = -y$$
    $$y' = x * 1 + y * 0  = x$$

    То есть, поворот на 90 градусов против часовой стрелки дает:

    $$x' = -y$$
    $$y' = x$$

2. Поворот на 90 градусов по часовой стрелке:

    Поворот на 90 градусов по часовой стрелке эквивалентен повороту на -90 градусов (θ = -π/2 радиан или -90°). В этом случае:

    $$cos(-π/2) = 0$$
    $$sin(-π/2) = -1$$

    Подставляя эти значения в общие формулы поворота, получаем:

    $$x' = x * 0 - y * (-1) = y$$
    $$y' = x * (-1) + y * 0 = -x$$

    То есть, поворот на 90 градусов по часовой стрелке дает:

    $$x' = y$$
    $$y' = -x$$


```python
class Rectangle:
    def __init__(self, corner, opposite_corner):
        self.x = min(corner[0], opposite_corner[0]) 
        self.y = max(corner[1], opposite_corner[1])
        self.width = abs(corner[0] - opposite_corner[0])
        self.height = abs(corner[1] - opposite_corner[1])
    
    def area(self):
        result = self.width * self.height
        return round(result, 2)
    
    def perimeter(self):
        result = (self.width + self.height) * 2
        return round(result, 2)

    def get_pos(self):
        return round(self.x, 2), round(self.y, 2)
    
    def get_size(self):
        return round(self.width, 2), round(self.height, 2)
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def resize(self, width, height):
        self.width, self.height = width, height
        
    def turn(self):
        center_x = self.x + self.width / 2
        center_y = self.y - self.height / 2

        # Координаты углов (левый верхний и правый нижний)
        x1 = self.x
        y1 = self.y
        x2 = self.x + self.width
        y2 = self.y - self.height

        # Выполняем поворот
        x1_prime = x1 - center_x
        y1_prime = y1 - center_y
        x1_rotated = y1_prime
        y1_rotated = -x1_prime
        x1_final = x1_rotated + center_x
        y1_final = y1_rotated + center_y

        x2_prime = x2 - center_x
        y2_prime = y2 - center_y
        x2_rotated = y2_prime
        y2_rotated = -x2_prime
        x2_final = x2_rotated + center_x
        y2_final = y2_rotated + center_y

        # Обновляем атрибуты прямоугольника
        self.x = round(min(x1_final, x2_final), 2)
        self.y = round(max(y1_final, y2_final), 2)
        self.width = round(abs(x1_final - x2_final), 2)
        self.height = round(abs(y1_final - y2_final), 2)

    def scale(self, factor):
        center_x = self.x + self.width / 2
        center_y = self.y - self.height / 2

        # Новые размеры
        new_width = self.width * factor
        new_height = self.height * factor

        # Новые координаты левого верхнего угла
        new_x = center_x - new_width / 2
        new_y = center_y + new_height / 2

        # Обновляем атрибуты прямоугольника
        self.x = round(new_x, 2)
        self.y = round(new_y, 2)
        self.width = round(new_width, 2)
        self.height = round(new_height, 2)
```

H. Шашки
```python
class Cell:
    def __init__(self, state):
        self.state = state

    def status(self):
        return self.state


class Checkers:
    def __init__(self):
        self.cells = {}
        for row in "12345678":
            for col in "ABCDEFGH":
                p = col + row
                if (row in "68" and col in "BDFH") or (row == "7" and col in "ACEG"):
                    self.cells[p] = Cell("B")
                elif (row in "13" and col in "ACEG") or (row == "2" and col in "BDFH"):
                    self.cells[p] = Cell("W")
                else:
                    self.cells[p] = Cell("X")

    def move(self, f, t):
        self.cells[t].state = self.cells[f].state
        self.cells[f].state = "X"

    def get_cell(self, p):
        return self.cells[p]
```

I. Очередь
```python
class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def pop(self):
        return self.items.pop(0)
    
    def push(self, item):
        self.items.append(item)
```

J. Стек
```python
class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def pop(self):
        return self.items.pop()
    
    def push(self, item):
        self.items.append(item)
```