import redis

client = redis.Redis(host='localhost', port=6379)

pipeline = client.pipeline()

pipeline.set('key1', 'value1')
pipeline.set('key2', 'value2')
pipeline.set('key3', 'value3')

results = pipeline.execute()

for result in results:
    print(result)

print(client.get('key1'))  # b'value1'
print(client.get('key2'))  # b'value2'
print(client.get('key3'))  # b'value3'
