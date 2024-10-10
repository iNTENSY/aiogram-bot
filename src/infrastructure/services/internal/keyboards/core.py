import abc


class AbstractTelegramKeyboard(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def generate_keyboard(self, *args, **kwargs) -> ...:
        ...
