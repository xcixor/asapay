from django import template

register = template.Library()


@register.filter
def check_payment_status(response_message):
    if response_message and response_message != "NULL":
        return get_status(response_message)
    return "N/A"

def get_status(message):
    if "successfully" in message.lower():
        return "Successful"
    elif "cancelled" in message.lower():
        return "Cancelled by user"
    return "Failed"