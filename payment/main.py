from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# In term microservices it should be a new database, but free redis plan not allow it
redis = get_redis_connection(
    host="redis-14441.c267.us-east-1-4.ec2.cloud.redislabs.com",
    port="14441",
    password="jCVLJWxhhx1Ceyq8SQqdsSX1aULqqNkz",
    decode_responses=True
)

class Order(HashModel):
    product_id: str
    price: float
    fee: float
    total: float
    quatity: int
    status: str # penfing, completed, refunded
    
    class Meta: 
        database = redis
