from rest_framework.test import APISimpleTestCase, APITestCase
from django.urls import reverse, resolve
from api.views import *


class PlayerTestCase(APITestCase):

    def setUp(self):
        self.user = self.client.post('/api/auth/users/', data={'username': 'Dima', 'password': 'Qweasd123dds'})
        response = self.client.post('/api/auth/jwt/create/', data={'username': 'Dima', 'password': 'Qweasd123dds'})
        self.token = response.data['access']
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_player_profile(self):
        player_data = {'description': 'I am a new player'}
        response = self.client.put(reverse('player', kwargs={'pk': 1}), data=player_data)
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_player_home(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_add_pokemon(self):
        def test_player_home(self):
            url = reverse('home')
            data = {'pokemon_name': 'pikachu'}
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, 201)

    def test_player_list(self):
        url = reverse('list-player')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)



