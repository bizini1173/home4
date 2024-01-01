from typing import List

class UserController:
    def create(self, surname, firstname, patronymic):
        pass
    
class User:
    def __init__(self, surname, firstname, patronymic):
        self.surname = surname
        self.firstname = firstname
        self.patronymic = patronymic

    def __str__(self):
        return f"{self.surname} {self.firstname} {self.patronymic}"

class Teacher(User):
    def __init__(self, teacher_id, surname, firstname, patronymic):
        super().__init__(surname, firstname, patronymic)
        self.teacher_id = teacher_id

    def get_teacher_id(self):
        return self.teacher_id

    def __str__(self):
        return f"Teacher ID: {self.teacher_id}, {super().__str__()}"

class TeacherService:
    def __init__(self):
        self.teacher_list = []
        self.max_teacher_id = 0

    def get_all(self):
        return self.teacher_list

    def init_data(self, teacher_list):
        self.teacher_list = teacher_list
        self.max_teacher_id = max([teacher.get_teacher_id() for teacher in self.teacher_list], default=0)

    def create(self, surname, firstname, patronymic):
        teacher = Teacher(self.max_teacher_id + 1, surname, firstname, patronymic)
        self.max_teacher_id += 1
        self.teacher_list.append(teacher)

    def edit_teacher(self, teacher_id, surname, firstname, patronymic):
        for teacher in self.teacher_list:
            if teacher.get_teacher_id() == teacher_id:
                teacher.set_surname(surname)
                teacher.set_firstname(firstname)
                teacher.set_patronymic(patronymic)

class TeacherView:
    def send_on_console(self, teacher_list):
        for teacher in teacher_list:
            print(teacher)

class TeacherController(UserController):
    def __init__(self):
        self.teacher_service = TeacherService()
        self.teacher_view = TeacherView()

    def create(self, surname, firstname, patronymic):
        self.teacher_service.create(surname, firstname, patronymic)

    def edit_teacher(self, teacher_id, surname, firstname, patronymic):
        self.teacher_service.edit_teacher(teacher_id, surname, firstname, patronymic)

    def init_teacher_list(self, teacher_list):
        self.teacher_service.init_data(teacher_list)

    def print_teachers(self):
        self.teacher_view.send_on_console(self.teacher_service.get_all())

# Пример использования:

teacher_controller = TeacherController()

# Инициализация списка учителей
teachers = [Teacher(1, "Ivanov", "Ivan", "Ivanovich"), Teacher(2, "Petrov", "Petr", "Petrovich")]
teacher_controller.init_teacher_list(teachers)

# Вывод списка учителей
teacher_controller.print_teachers()

# Создание нового учителя
teacher_controller.create("Sidorov", "Sidor", "Sidorovich")
teacher_controller.create("Mirovaev", "Miron", "Mironovich")

# Вывод обновленного списка учителей
teacher_controller.print_teachers()
