import redis

client = redis.Redis(host='localhost', port=6379)

pipeline = client.pipeline()

pipeline.hset('key1', "field1", "value1")
pipeline.hset('key2', "field2", "value2")
pipeline.hset('key3', "field3", "value3")

results = pipeline.execute()
