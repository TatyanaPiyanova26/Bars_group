from behave import *
from django.contrib.auth.models import Group, User


@given('admin user is authenticated')
def admin_user_authenticated(context):
    login = 'admin'
    password = 'admin12345!'
    User.objects.create_superuser(username=login, password=password)
    context.response = context.test.client.login(username=login, password=password)


@when('user creates "{group_name}"')
def add_new_group(context, group_name):
    context.test.client.post('/admin/auth/group/add/', {'name': group_name})


@then('group list is "{groups_str_list}"')
def verify_group_added(context, groups_str_list):
    verify_groups = Group.objects.all()
    for group in groups_str_list.split(','):
        assert verify_groups.filter(name=group).exists() is True


@given('there are groups "{groups_str_list}"')
def get_groups(context, groups_str_list):
    groups = groups_str_list.split(',')
    for group in groups:
        Group.objects.create(name=group)


@when('user deletes the "{group}"')
def delete_group(context, group):
    del_group = list(Group.objects.values('id', 'name').filter(name=group))[0]
    id_group = del_group['id']
    url = '/admin/auth/group/%s/delete/' % id_group
    context.test.client.post(url, {'post': 'yes'})


@then('group list does not contain the deleted group "{group}"')
def verify_deleted_group_does_not_exist(context, group):
    groups = Group.objects.all()
    assert groups.filter(name=group).exists() is False
