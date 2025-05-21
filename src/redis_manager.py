from redis_om import get_redis_connection, HashModel

from src.config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD


redis = get_redis_connection(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD
)


class Order(HashModel):
    product_id: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str # pending, completed, refunded

    class Meta:
        database = redis
