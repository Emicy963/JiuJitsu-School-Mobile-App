import flet as ft
from .controllers import AcademyController

class AcademyViews:
    def __init__(self, page: ft.Page, controller: AcademyController):
        self.page = page
        self.controller = controller
        self.page.title = 'Academy App'
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER

        # Initiallizer UI Components
        ## Create View
        self.name_field = ft.TextField(label='Nome')
        self.email_field = ft.TextField(label='Email')
        self.belt_field = ft.TextField(label='Faixa')
        self.date_birth_field = ft.TextField(label='Data de Nascimento(YYYY-MM-DD)')
        self.create_result = ft.Text()
        ## List View
        self.student_table = self.create_student_table()
        ## Add Classes View
        self.email_class_field = ft.TextField(label='Email do aluno')
        self.qtd_class_field = ft.TextField(label='Quantidade de aulas', value=1)
        self.class_result = ft.Text()
        ## Add Student Progress View
        self.email_progress_field = ft.TextField(label='Email do aluno')
        self.progress_result = ft.Text()
        ## Update Student
        self.id_student_field = ft.TextField(label='ID Aluno')
        name_update_field = ft.TextField(label='Novo nome')
        email_update_field = ft.TextField(label='Novo email')
        belt_update_field = ft.TextField(label='Nova faixa')
        date_update_field = ft.TextField(label='Nova data de nascimento')
        self.update_result = ft.Text()

    def create_student_table(self):
        return ft.DataTable(
            columns= [
                ft.DataColumn(ft.Text('Name')),
                ft.DataColumn(ft.Text('Email')),
                ft.DataColumn(ft.Text('Faixa')),
                ft.DataColumn(ft.Text('Data de Nascimento')),
            ], rows=[]
        )
