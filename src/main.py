import flet as ft
from .models import AcademyModel
from .controllers import AcademyController
from .views import AcademyViews

API_BASE_URL = 'http://localhost:8000/api/'

def main(page: ft.Page):
    model = AcademyModel(API_BASE_URL)
    controller = AcademyController(model)
    view = AcademyViews(page, controller)
    page.add(view.build())

if __name__=='__main__':
    ft.app(target=main)
