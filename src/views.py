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
        self.list_result = ft.Text()
        ## Add Classes View
        self.email_class_field = ft.TextField(label='Email do aluno')
        self.qtd_class_field = ft.TextField(label='Quantidade de aulas', value=1)
        self.class_result = ft.Text()
        ## Add Student Progress View
        self.email_progress_field = ft.TextField(label='Email do aluno')
        self.progress_result = ft.Text()
        ## Update Student
        self.id_student_field = ft.TextField(label='ID Aluno')
        self.name_update_field = ft.TextField(label='Novo nome')
        self.email_update_field = ft.TextField(label='Novo email')
        self.belt_update_field = ft.TextField(label='Nova faixa')
        self.date_update_field = ft.TextField(label='Nova data de nascimento')
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
    
    def build(self):
        return ft.Tabs(
            selected_index=0,
            tabs=[
                ft.Tab(text='Listar Aluno', content=self.list_student_tab())
            ]
        )
    
    # Tabs views
    def list_student_tab(self):
        return ft.Column([
            self.list_student_tab,
            self.list_result,
            ft.ElevatedButton(text='Listar Alunos', on_click=True)
        ], scroll=True)
    
    def list_student_click(self, e):
        try:
            students = self.controller.handle_get_all_student().json()

            self.student_table.rows.clear()

            for student in students:
                row = ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(student.get('name'))),
                        ft.DataCell(ft.Text(student.get('email'))),
                        ft.DataCell(ft.Text(student.get('bet'))),
                        ft.DataCell(ft.Text(student.get('date_birth'))),
                    ]
                )
                self.student_table.rows.append(row)
            self.list_result.value = 'Sucess found students'
            self.page.update()
        except Exception as err:
            self.list_result.value = f'Erro: {str(err)}'
            self.page.update()
