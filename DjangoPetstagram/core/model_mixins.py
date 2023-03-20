class StrRepresentationMixin:
    repr_columns = ()

    def __str__(self):
        res = ', '.join(f'{str_value}: {getattr(self, str_value, None)}' for str_value in self.repr_columns)
        return res


# Accounts model mixins
class GetEnumValuesMixin:
    @classmethod
    def get_values(cls):
        return [(x.name, x.value) for x in cls]


class GetEnumMaxLenValueMixin:
    @classmethod
    def max_length(cls):
        return max(len(x.value) for x in cls)