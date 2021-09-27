import unittest

from django.test import Client


class EventoTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_nao_pode_faltar_from(self):
        response = self.client.get("/api?to=EUR&amount=123.45", follow=True)
        esperado = {
            "status": "error",
            "msg": "Os seguintes parâmetros estão faltando: from",
        }

        self.assertEqual(response.data, esperado)
        self.assertEqual(response.status_code, 400)

    def test_nao_pode_faltar_to(self):
        response = self.client.get("/api?from=EUR&amount=123.45", follow=True)
        esperado = {
            "status": "error",
            "msg": "Os seguintes parâmetros estão faltando: to",
        }

        self.assertEqual(response.data, esperado)
        self.assertEqual(response.status_code, 400)

    def test_nao_pode_faltar_amount(self):
        response = self.client.get("/api?from=EUR&to=BTC", follow=True)
        esperado = {
            "status": "error",
            "msg": "Os seguintes parâmetros estão faltando: amount",
        }

        self.assertEqual(response.data, esperado)
        self.assertEqual(response.status_code, 400)

    def test_nao_pode_faltar_dois_parametros(self):
        response = self.client.get("/api?from=EUR", follow=True)
        esperado = {
            "status": "error",
            "msg": "Os seguintes parâmetros estão faltando: amount, to",
        }

        self.assertEqual(response.data, esperado)
        self.assertEqual(response.status_code, 400)

    def test_nao_pode_faltar_nenhum_parametros(self):
        response = self.client.get("/api", follow=True)
        esperado = {
            "status": "error",
            "msg": "Os seguintes parâmetros estão faltando: amount, from, to",
        }

        self.assertEqual(response.data, esperado)
        self.assertEqual(response.status_code, 400)

    def test_nao_converter_mesma_moeda(self):
        response = self.client.get("/api?from=USD&to=USD&amount=2", follow=True)
        esperado = {
            "status": "error",
            "msg": "Não é possível transmitir para a mesma moeda",
        }

        self.assertEqual(response.data, esperado)
        self.assertEqual(response.status_code, 400)

    def test_nao_tem_suporte(self):
        response = self.client.get("/api?from=USD&to=ETL&amount=2", follow=True)
        esperado = {
            "status": "error",
            "msg": "Não temos suporte para o tipo de moeda ETL",
        }

        self.assertEqual(response.data, esperado)
        self.assertEqual(response.status_code, 400)
