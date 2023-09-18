from django.test import TestCase
from django.test import SimpleTestCase
from .models import Laboratorio
from django.urls import reverse

# Create your tests here.

class InicioTest(SimpleTestCase):

    def test_url_exists_at_correct_location(self):
        response = self.client.get('/formadd/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('formadd'))
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self):
        response = self.client.get(reverse('formadd'))
        self.assertTemplateUsed(response, 'lab.html')
    
    #NO PUDE PONER EL CODIGO HTML 
    # def test_template_content(self):
    #     response = self.client.get(reverse('/formadd/'))
    #     self.assertContains(response, '')
    #     self.assertNotContains(response, 'No es la pagina')

class PersonaTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.persona =  Laboratorio.objects.create(nombre = 'Laboratorio test',
                                              ciudad = 'ciudadTest',
                                              pais='paisTest')
    
    def test_model_content(self):
        self.assertEqual(self.persona.nombre, 'Laboratorio test')
        self.assertEqual(self.persona.ciudad, 'ciudadTest')
        self.assertEqual(self.persona.pais, 'paisTest')