from behave import *
from django.contrib.auth.models import User
from bs4 import BeautifulSoup


@when('user opens page "{url}"')
def open_page(context, url):
    context.response = context.test.client.get('/admin/')


@then('user is redirected to "{url}"')
def redirect_to_url(context, url):
    assert context.response.status_code == 302
    assert context.response['Location'] == url


@given('admin user with username "{login}" and password "{password}"')
def create_admin_user(context, login, password):
    User.objects.create_superuser(username=login, password=password)


@when('user logins with username "{login}" and password "{password}"')
def log_in(context, login, password):
    context.response = context.test.client.post('/admin/login/', {'username': login, 'password': password})


@then('page loaded successfully')
def load_success(context):
    assert context.response.status_code == 200


@then('failed to login')
def error_log_in(context):
    soup = BeautifulSoup(context.response.content.decode('utf-8'))
    msg = soup.find('p', {'class': 'errornote'}).text
    assert context.response.status_code == 200
    assert 'Please enter the correct username and password for a staff account' in msg

