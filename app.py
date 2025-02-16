import flet as ft
import requests

API_BASE_URL = 'http://localhost:8000/api/'

def main(page: ft.Page):
    page.title = 'Exemple'
    
    """ Creat Student aba """
    name_field = ft.TextField(label='Nome')
    email_field = ft.TextField(label='Email')
    belt_field = ft.TextField(label='Faixa')
    date_birth_field = ft.TextField(label='Data de Nascimento (YYYY-MM-DD)')
    creat_result = ft.Text()
    
    def creat_student(e):
        payload = {
            'name': name_field.value,
            'email': email_field.value,
            'belt': belt_field.value,
            'date_birth': date_birth_field.value
        }

        response = requests.post(API_BASE_URL + '', json=payload)
        if response.status_code == 200:
            student = response.json()
            creat_result.value = f'Aluno Criado: {student}'
        else:
            creat_result.value = f'Erro: {response.text}'

        page.update()

    creat_button = ft.ElevatedButton(text='Criar Aluno', on_click=creat_student)

    creat_student_tab = ft.Column(
        [
            name_field,
            email_field,
            belt_field,
            date_birth_field,
            creat_result,
            creat_button,
        ],
        scroll=True
    )

    """List student aba"""
    student_table = ft.DataTable(
        columns= [
            ft.DataColumn(ft.Text('Nome')),
            ft.DataColumn(ft.Text('Email')),
            ft.DataColumn(ft.Text('Faixa')),
            ft.DataColumn(ft.Text('Data de Nascimento')),
        ],
        rows=[]
    )

    def list_student_click(e):
        response = requests.get(API_BASE_URL + 'students/')
        students = response.json()
        
        student_table.rows.clear()

        for student in students:
            row = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(student.get('name'))),
                    ft.DataCell(ft.Text(student.get('email'))),
                    ft.DataCell(ft.Text(student.get('belt'))),
                    ft.DataCell(ft.Text(student.get('date_birth'))),
                ]
            )
            student_table.rows.append(row)
        list_result.value = f'{len(students)} alunos encontrados'
        page.update()

    list_result = ft.Text()
    list_button = ft.ElevatedButton(text='Lista Alunos', on_click=list_student_click)
    list_student_tab = ft.Column(
        [student_table, list_result, list_button],
        scroll=True
    )

    """ Add Classes """

    email_class_field = ft.TextField(label='Email do aluno')
    qtd_class_field = ft.TextField(label='Quantidades de aulas', value=1)
    class_result = ft.Text()

    def book_class_click(e):
        payload = {
            'qtd': int(qtd_class_field.value),
            'email_student': email_class_field.value
        }

        response = requests.post(API_BASE_URL + 'class_held/', json=payload)
        
        if response.status_code == 200:
            class_result.value = f'Sucesso: {response.json()}'
        else:
            class_result.value = f'Erro: {response.text}'
        
        page.update()

    class_button = ft.ElevatedButton(text='Marcar aula realizada', on_click=book_class_click)
    class_tab = ft.Column([email_class_field, qtd_class_field, class_result, class_button], scroll=True)

    """ Student Progress """

    email_progress_field = ft.TextField(label='Email do aluno')
    progress_result = ft.Text()

    def consult_progress_click(e):
        email = email_progress_field.value
        response = requests.get(API_BASE_URL + 'progress_student/', params={'email_student': email})
        if response.status_code == 200:
            progress = response.json()
            progress_result.value = (
                f'Nome: {progress.get('name')}\n'
                f'Email: {progress.get('email')}\n'
                f'Faixa: {progress.get('belt')}\n'
                f'Total de aulas: {progress.get('total_class')}\n'
                f'Aulas necessárias para a próxima faixa: {progress.get('class_for_next_belt')}'
            )
        else:
            progress_result.value = f'Erro: {response.text}'
        page.update()

    progress_button = ft.ElevatedButton(text='Consultar progresso', on_click=consult_progress_click)
    progress_tab = ft.Column([email_progress_field, progress_result, progress_button], scroll=True)

    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text='Criar Aluno', content=creat_student_tab),
            ft.Tab(text='Listar Aluno', content=list_student_tab),
            ft.Tab(text='Cadastrar aula', content=class_tab),
            ft.Tab(text='Progresso do aula', content=progress_tab),
        ]
    )

    page.add(tabs)

if __name__ == '__main__':
    ft.app(target=main)
