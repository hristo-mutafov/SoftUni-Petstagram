class StrRepresentationMixin:
    repr_columns = ()

    def __str__(self):
        return ', '.join(f'{str_value}: {getattr(self, str_value, None)}' for str_value in self.repr_columns)

