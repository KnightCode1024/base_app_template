from dishka import Provider, Scope, provide

from core.uow import UnitOfWork
from repositories import (
    IUserRepository,
)
from services import (
    UserService,
)


class ServiceProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def get_user_service(
        self,
        uow: UnitOfWork,
        user_repository: IUserRepository,
    ) -> UserService:
        return UserService(uow, user_repository)
