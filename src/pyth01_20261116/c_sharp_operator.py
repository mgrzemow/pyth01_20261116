class Maybe:
    def __init__(self, value):
        self._value = value

    def __getattr__(self, name):
        if self._value is None:
            return Maybe(None)
        return Maybe(getattr(self._value, name))

    def __getitem__(self, key):
        if self._value is None:
            return Maybe(None)
        return Maybe(self._value[key])

    def __call__(self, *args, **kwargs):
        if self._value is None:
            return Maybe(None)
        return Maybe(self._value(*args, **kwargs))

    def unwrap(self, default=None):
        return default if self._value is None else self._value


# C#: user?.Address?.City ?? "brak"
# miasto = Maybe(user).address.city.unwrap("brak")
