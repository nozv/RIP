from pdf_gen.pdf_gen import pdf
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    r = Rectangle(16, 16, "Синий")
    c = Circle(16, "Зеленый")
    s = Square(16, "Красный")
    print(r)
    print(c)
    print(s)
    file = pdf('C:/Users/user/PycharmProjects/RIP/LR2', 'pdfka')
    file.insert_image('C:/Users/user/PycharmProjects/RIP/LR2/102.jpg', width=400, height=300)
    file.save()


if __name__ == "__main__":
    main()

