from django import template
register = template.Library()

@register.filter
def date_mask(value):
    return value.strftime('%d/%m/%Y')

@register.filter
def datefull_mask(value):
    mes = ""
    if value.month == 1:
        mes = "Janeiro"
    elif value.month == 2:
        mes = "Fevereiro"
    elif value.month == 3:
        mes = "Março"
    elif value.month == 4:
        mes = "Abril"
    elif value.month == 5:
        mes = "Maio"
    elif value.month == 6:
        mes = "Junho"
    elif value.month == 7:
        mes = "Julho"
    elif value.month == 8:
        mes = "Agosto"
    elif value.month == 9:
        mes = "Setembro"
    elif value.month == 10:
        mes = "Outubro"
    elif value.month == 11:
        mes = "Novembro"
    elif value.month == 12:
        mes = "Dezembro"
    return value.strftime('%d de ') + str(mes) + value.strftime(' de %Y')

@register.filter
def datetime_mask(value):
    return value.strftime('%d/%m/%Y %H:%M')
