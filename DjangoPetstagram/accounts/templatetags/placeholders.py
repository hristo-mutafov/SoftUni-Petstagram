from django import template, forms

register = template.Library()

@register.filter
def placeholder(value, text):
    value.field.widget.attrs['placeholder'] = text
    if text == 'mm/dd/yyyy':
        value.field.widget = forms.DateInput(attrs={'type': 'date', 'placeholder': text})
    return value
