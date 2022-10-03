from django.test import TestCase

# Create your tests here.

class TestarPaginas(TestCase):
    def testar_se_pagina_principal_carrega_completamente(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)