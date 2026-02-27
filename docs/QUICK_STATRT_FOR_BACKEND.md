# Описание бэкенд проекта

## Архитектура

## Права доступа

Применяется в сервисном слое. В параметрах декораторо нужно указать списком роли, кому разрешён доступ к этому ресурсу.

```python
class UserService:
    ...

    @require_roles([RoleEnum.ADMIN])
    async def get_all_users(
            self,
            user: UserResponse,
            offset: int = 0,
            limit: int = 20,
    ):
        users = await self.user_repository.get_all(offset, limit)
        if not users:
            raise ValueError("Not a single user was found")
        return users
```

## Ограничитель запросов

Декоратор применяется в роутерах. Есть 2 стратегии блокировки: user id и ip address.

```python
from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter, Request

from core.rate_limiter import RateLimiter, Strategy, rate_limit

router = APIRouter(
    prefix="",
    tags=["Dev Tools"],
    route_class=DishkaRoute,
)

@router.get("/ping")
@rate_limit(strategy=Strategy.IP, policy="30/s;200/m;3000/h")
# Так же есть стратегия ограничения по user id (Strategy.USER)
async def pong(
        request: Request, # Обязательно передавать этот параметр в функцию
        rate_limiter: FromDishka[RateLimiter],# Обязательно передавать этот параметр в функцию
):
    return {"msg": "pong"}
```

## Внедрение нового функционала
