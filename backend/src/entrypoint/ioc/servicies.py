from dishka import Provider, Scope, provide

from core.uow import UnitOfWork
from entrypoint.config import Config
from interfaces import IEmailService
from repositories import (
    IUserRepository,
    )
from services import (
    EmailService,
    UserService,
)


class ServiceProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def get_user_service(
        self,
        uow: UnitOfWork,
        user_repository: IUserRepository,
        email_service: IEmailService,
    ) -> UserService:
        return UserService(uow, user_repository, email_service)

    @provide
    def get_email_service(self, config: Config) -> IEmailService:
        return EmailService(config)

