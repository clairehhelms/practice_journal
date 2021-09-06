"""Lesson days class."""

class Lesson:
    lesson_characteristics: list[str] = ["date", "scales and warmups", "scales goals", "etudes and exercises", "exercises goals", "repertoire", "rep goals", "other"]
    lesson_dict: dict[str, str] = {}

    def __init__ (self):
        for item in self.lesson_characteristics:
            self.lesson_dict[item] = input("Today's " + item + ": ")