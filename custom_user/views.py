from authlib.oauth2.rfc6749 import OAuth2Token
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render, redirect
from django.urls import reverse
from urllib.parse import quote_plus, urlencode

from custom_user.models import CustomUser

oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)


# def callback(request: HttpRequest) -> HttpResponse:
#     """"""
#     return HttpResponse("This is a callback.")


def callback(request: HttpRequest):
    """
    {'access_token': '',
    'id_token': '',
     'scope': 'openid profile email',
     'expires_in': 86400,
     'token_type': 'Bearer',
     'expires_at': 1653407436,
     'userinfo': {'given_name': 'bivu', 'family_name': 'raj', 'nickname': 'bivujob', 'name': 'bivu raj', 'picture': 'https://lh3.googleusercontent.com/a/AATXAJyqWiu-dqugSXYKexBnqGeDX_m7f7KKf1WICtE9=s96-c', 'locale': 'en', 'updated_at': '2022-05-23T15:48:09.800Z', 'email': 'bivujob@gmail.com', 'email_verified': True, 'iss': 'https://rajbabu.auth0.com/', 'sub': 'google-oauth2|106818687261459369890', 'aud': 'cH9aDmhF5uQ3DAb8smXWUqpug4ePqt6F', 'iat': 1653321035, 'exp': 1653357035, 'nonce': 'tguRznaUPMnx4Xh2APR9'}}
    """
    token: OAuth2Token = oauth.auth0.authorize_access_token(request)
    custom_user, _ = CustomUser.objects.get_or_create(email=token['userinfo']['email'])
    django_login(request, custom_user)
    request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse("index")))


# def logout_user(request: HttpRequest) -> HttpResponse:
#     """"""
#     user = request.user
#     if user.is_authenticated:
#         logout(request)
#     return HttpResponseRedirect("/")


def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )


def logout(request: HttpRequest):

    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("index")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )


def check_login(request: HttpRequest) -> HttpResponse:
    return HttpResponse(str(request.user.is_authenticated))