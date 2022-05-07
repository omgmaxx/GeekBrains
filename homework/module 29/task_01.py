import functools
from typing import Callable


def check_permission(permission: str = 'guest') -> Callable:
    """
    Декоратор, проверяющий, обладает ли юзер соответствующими правами.
    """
    def permission_decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            if permission in user_permissions:
                res = func(*args, **kwargs)
            else:
                raise PermissionError(f'У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')
            return res
        return wrapped
    return permission_decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
