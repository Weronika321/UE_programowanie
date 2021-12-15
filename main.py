import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = (
    r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
)


def read_text(filename: str) -> str:
    img_cv = cv2.imread(filename)
    img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
    return pytesseract.image_to_string(img_rgb)


paths = [
    "img\\text_1.jpg",
    "img\\text_2.png",
    "img\\text_3.png",
    "img\\text_4.png",
    "img\\text_5.png",
]

[print(read_text(path)) for path in paths]
