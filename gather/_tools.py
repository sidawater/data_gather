from functools import wraps


def run_create(func):
    """
    as a instance methods' decorator
    run instance._create before run func
    """
    @wraps(func)
    def _run_pre(self, *args, **kwargs):
        self._create()
        return func(self, *args, **kwargs)
    return _run_pre
