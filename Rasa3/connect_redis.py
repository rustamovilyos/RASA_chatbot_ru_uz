import redis


redis_connection = redis.StrictRedis(
    host='localhost',
    port=6379,
    db=0,
    password=''
)
redis_connection.set('Lord', 'lord Ilyos')
data = redis_connection.get('service_name')
if data:
    print(data.decode('utf-8'))
else:
    print('key not found')
redis_connection.close()
