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
                ft.Tab(text='Novo Aluno', content=self.create_student_tab()),
                ft.Tab(text='Listar Aluno', content=self.list_student_tab()),
                ft.Tab(text='Cadastrar Aula', content=self.book_class_tab()),
                ft.Tab(text='Consultar Progresso', content=self.consult_progress_tab()),
                ft.Tab(text='Atualizar Aluno', content=self.update_student_tab()),
            ]
        )
    
    # Tabs views
    ## Create Tab
    def create_student_tab(self):
        return ft.Column([
            self.name_field,
            self.email_field,
            self.belt_field,
            self.date_birth_field,
            ft.ElevatedButton(text='Novo Aluno', on_click=self.create_student_click)
        ], scroll=True)
    
    ## List Student Tab
    def list_student_tab(self):
        return ft.Column([
            self.list_student_tab,
            self.list_result,
            ft.ElevatedButton(text='Listar Alunos', on_click=self.list_student_click)
        ], scroll=True)
    
    ## Add Classes Progress tab
    def book_class_tab(self):
        return ft.Column([
            self.email_class_field,
            self.qtd_class_field,
            ft.ElevatedButton(text='Marcar aula realizada!', on_click=self.book_class_click),
            self.class_result,
        ], scroll=True)
    
    ## Student Progress Tab
    def consult_progress_tab(self):
        return ft.Column([
            self.email_progress_field,
            ft.ElevatedButton(text='Consultar progresso', on_click=self.consult_progres_click),
            self.progress_result,
        ], scroll=True)
    
    ## Update Student Tab
    def update_student_tab(self):
        return ft.Column([
            self.id_student_field,
            self.name_update_field,
            self.email_update_field,
            self.belt_update_field,
            self.date_update_field,
            ft.ElevatedButton(text='Atualizar Aluno', on_click=self.update_student_click),
            self.update_result,
        ], scroll=True)
    
    # Click methods
    ## Create click method
    def create_student_click(self, e):
        try:
            response = self.controller.handle_create_student(self.name_field.value, self.email_field.value, self.belt_field.value, self.date_birth_field.value)

            self.create_result.value = 'Create student sucess!' if response.status_code==200 else 'Erro ao criar o aluno!'
            self.page.update()
        except Exception as err:
            self.create_result.value = f'Erro: {str(err)}'
            self.page.update()
    
    ## List student click method
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

    ## Class Progress Click
    def book_class_click(self, e):
        try:
            response = self.controller.handle_book_class(self.qtd_class_field.value, self.email_class_field.value)

            self.class_result.value = f'Sucesso' if response.status_code == 200 else 'Erro ao resgitrar o progresso do aluno'
            self.page.update()
        except Exception as err:
            self.class_result.value = f'Erro: {str(err)}'
            self.page.update()

    ## Conult Progress Click
    def consult_progres_click(self, e):
        try:
            response = self.controller.handle_consult_progress(self.email_progress_field)
            progress = response.json()
            self.progress_result.value = (
                f'Nome: {progress.get('name')}\n',
                f'Email: {progress.get('email')}\n',
                f'Faixa: {progress.get('belt')}\n',
                f'Total de aulas: {progress.get('total_class')}\n',
                f'Aulas necessária para a próxima faixa: {progress.get('class_for_next_belt')}'
            ) if response.status_code == 200 else f'Erro ao consultar aluno: {response.text}'
            self.page.update()
        except Exception as err:
            self.progress_result.value = f'Erro: {str(err)}'
            self.page.update()

    ## Update Student Click
    def update_student_click(self, e):
        try:
            id_student = self.id_student_field.value
            if not id_student:
                self.update_result.value = 'ID do Aluno é obrigatório'
            else:
                response = self.controller.handle_update_student(id_student, self.name_update_field.value, self.email_update_field, self.belt_update_field, self.date_update_field.value)
                student = response.json()
                self.update_result.value = f'Aluno atualizado com sucesso: {student.get('name')}' if response.status_code==200 else f'Erro ao atualizar aluno: {response.text}'
            self.page.update()
        except Exception as err:
            self.update_result.value = f'Erro: {str(err)}'
            self.page.update()
