from django.core.exceptions import ValidationError


def validar_precio(value):
    if 9 <= value <= 25:
        raise ValidationError(
            '%(value)s El precio del plato debe de estar entre 9 y 25 Dolares',
            params={'value': value},
        )
