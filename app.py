import flet as ft
import requests

API_BASE_URL = 'http://localhost:8000/api/'

def main(page: ft.Page):
    page.title = 'Exemple'

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

    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text='Criar Aluno', content=creat_student_tab)
        ]
    )

    page.add(tabs)

if __name__ == '__main__':
    ft.app(target=main)
