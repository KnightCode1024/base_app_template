__all__ = ["broker"]

from taskiq_aio_pika import AioPikaBroker
# from taskiq.middlewares.taskiq_admin_middleware import TaskiqAdminMiddleware

from entrypoint.config import config

broker = AioPikaBroker(
    url=config.rabbitmq.URL,
)
# .with_middlewares(
#         TaskiqAdminMiddleware(
#             url="http://localhost:3000",
#             api_token="supersecret",
#             taskiq_broker_name="mybroker",
#         )
# )