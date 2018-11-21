import redis

r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)

r.set('name', 'ice')
r.mset({'name': 'rick', 'age': '25', 'gender': '1'})
r.append('name', ' and vigo')
print(r.get('name'))
print(r.mget('age', 'gender'))

# hashSet
r.hmset('names', {'name1': 'ice', 'name2': 'rick', 'name3': 'vigo'})
print(r.hmget('names', 'name1', 'name2'))
print(r.hkeys('names'))
print(r.hvals('names'))

# list
r.delete('ages')
r.lpush('ages', 1, 2, 3)
for item in range(r.llen('ages')):
    print(r.lindex('ages', item))

# exist
print(r.exists('name2'))
print(r.exists('name'))
