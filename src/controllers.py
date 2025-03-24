from .models import AcademyModel

class AcademyController:
    def __init__(self, model:AcademyModel):
        self.model = model

    def handle_get_all_student(self):
        return self.model.get_all_student()
    
    def handle_create_student(self, name, email, belt, date_birth):
        return self.model.create_student(name, email, belt, date_birth)
    
    def handle_book_class(self, qtd, email_student):
        return self.model.book_class(qtd, email_student)
    
    def handle_consult_progress(self, email):
        return self.model.consult_progress(email)

    def handle_update_student(self, student_id, name, email, belt, date_birth):
        return self.model.update_student(student_id, name, email, belt, date_birth)
