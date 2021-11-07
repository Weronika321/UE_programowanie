class Student:
    def __init__(self, name: str, marks: int) -> None:
        self._name = name
        self._marks = marks

    @property
    def name(self):
        return self._name

    @property
    def marks(self):
        return self._marks

    def is_passed(self) -> bool:
        return self.marks > 50


student1 = Student('Adam', 56)
student2 = Student('Anna', 43)

print(f"{student1.name} zdał/a: {student1.is_passed()}")
print(f"{student2.name} zdał/a: {student2.is_passed()}")
