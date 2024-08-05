import redis

client = redis.Redis(host='localhost', port=6379)

print(client.set('key1', 'value1'))
print(client.set('key2', 'value2'))
print(client.set('key3', 'value3'))

print(client.get('key1'))  # b'value1'
print(client.get('key2'))  # b'value2'
print(client.get('key3'))  # b'value3'
