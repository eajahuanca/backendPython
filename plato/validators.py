from django.core.exceptions import ValidationError


def validar_precio(value):
    if value < 9.00 and value > 25.00:
        raise ValidationError(
            '%(value)s El precio del plato debe de estar entre 9 y 25 Dolares',
            params={'value': value},
        )
