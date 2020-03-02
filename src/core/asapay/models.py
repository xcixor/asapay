from django.db import models
from django.db import connection


def get_users():
    """fetch all users from database

    Returns:
        tuple -- list of users
    """
    with connection.cursor() as cursor:
        query = "SELECT * FROM users"
        cursor.execute(query)
        users = cursor.fetchall()
    return users

def get_users_total():
    """fetch users total from database

    Returns:
        int -- no of users
    """
    with connection.cursor() as cursor:
        query = "SELECT COUNT(*) FROM users"
        cursor.execute(query)
        users = cursor.fetchall()
    return users