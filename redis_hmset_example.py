import redis

client = redis.Redis(host='localhost', port=6379)

client.hset('key1', "field1", "value1")
client.hset('key2', "field2", "value2")
client.hset('key3', "field3", "value3")
