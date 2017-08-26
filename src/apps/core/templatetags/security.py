from django import template
register = template.Library()


@register.filter(name='has_jugador_group')
def has_jugador_group(user):
    return user.groups.filter(name='Jugador').exists()


@register.filter(name='has_administrador_group')
def has_administrador_group(user):
    return user.groups.filter(name='Administrador').exists()