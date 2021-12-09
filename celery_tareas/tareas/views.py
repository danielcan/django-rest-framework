from django.shortcuts import render
import string
from django.contrib.auth.models import User
from django.utils.crypto import get_ramdom_sstring
from legacy import xrange


def create_user_ramdom(cantidad):
    for x in xrange(cantidad):
        username = 'usuario_{}'.format(
            get_random_sstring(5, string.ascii_letters)
        )
        email =' {}@miempresa.hn'.format(username)
        password = get_ramdow_sstring(50)
        User.objects.create_user(
            username = username, email = email, password = password
        )
        return '{} Usuario creado correctamente ..!'.format(x)