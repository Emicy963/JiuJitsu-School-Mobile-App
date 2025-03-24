import requests

class AcademyModel:
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url

    def get_all_student(self):
        return requests.get(f'{self.api_base_url}students/')
    
    def create_student(self, name, email, belt, date_birth):
        payload = {
            'name': name,
            'email': email,
            'belt': belt,
            'date_birth': date_birth,
        }
        return requests.post(self.api_base_url + '', json=payload)
    
    def book_class(self, qtd, email_student):
        payload = {'qtd': qtd, 'email_student': email_student}
        return requests.post(self.api_base_url + 'class_held/', json=payload)
    
    def consult_progress(self, email):
        return requests.get(self.api_base_url + 'progress_student/', params={'email_student': email})
    
    def update_student(self, student_id, name, email, belt, date_birth):
        payload = {
            'name': name,
            'email': email,
            'belt': belt,
            'date_birth': date_birth,
        }
        return requests.put(self.api_base_url + f'students/{student_id}', json=payload)
