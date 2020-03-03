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


def get_airtime_purchases():
    """fetch all airtime payments

    Returns:
        tuple -- list of all airtime purchases
    """
    with connection.cursor() as cursor:
        query = "SELECT * FROM paymentDetails WHERE serviceID = %s ORDER BY dateCreated DESC" % 2
        cursor.execute(query)
        payments = cursor.fetchall()
    return payments


def get_kplc_purchases():
    """fetch all airtime payments

    Returns:
        tuple -- list of all airtime purchases
    """
    with connection.cursor() as cursor:
        query = "SELECT * FROM paymentDetails WHERE serviceID = %s ORDER BY dateCreated DESC" % 1
        cursor.execute(query)
        payments = cursor.fetchall()
    return payments


def get_airtime_purchases_total():
    """fetch users total from database

    Returns:
        int -- no of users
    """
    with connection.cursor() as cursor:
        query = "SELECT COUNT(*) FROM paymentDetails WHERE serviceID = %s" % 2
        cursor.execute(query)
        users = cursor.fetchall()
    return users


def get_kplc_purchases_total():
    """fetch users total from database

    Returns:
        int -- no of users
    """
    with connection.cursor() as cursor:
        query = "SELECT COUNT(*) FROM paymentDetails WHERE serviceID = %s" % 1
        cursor.execute(query)
        users = cursor.fetchall()
    return users