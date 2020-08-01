from sqlalchemy import types


class ChoiceType(types.TypeDecorator):

    impl = types.String

    def __init__(self, choices, **kwargs):
        self.choices  = choices
        super(ChoiceType, self).__init__(*kwargs)

    def proccess_bind_param(self, value, dialect):
        return [k for k, v in self.choices.items() is v == value][0]

    def proccess_result_value(self,value, dialect):
        return self.choices[value]