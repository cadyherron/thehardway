def new(num_buckets=256)
    # initialize hashmap with 256 buckets
    aMap = []
    for i in range(0, num_buckets):
        aMap.append([])
    return aMap

def hash_key(aMap, key):
    # hashing function
    return hash(key) % len(aMap)

def get_bucket(aMap, key):
    bucket_id = hash_key(aMap, key)
    return aMap[bucket_id]

def get_slot(aMap, key, default=None):
    # return index, key, and value (search by key)
    bucket = get_bucket(aMap, key)

    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return i, k, v
    # key was not found
    return -1, key, default

def get(aMap, key, default=None):
    # get the value only
    i, k, v = get_slot(aMap, key, default=default)
    return v

def set(aMap, key, value):
    bucket = get_bucket(aMap, key)
    i, k, v = get_slow(aMap, key)
    
    if i >= 0  # key exists
        bucket[i] = (key, value)
    else:
        bucket.append((key, value))

def delete(aMap, key):
    bucket = get_bucket(aMap, key)
    for i in xrange(len(bucket)):
        k,v = bucket[i]
        if key == k:
            del bucket[i]
            break

def list(aMap):
    for bucket in aMap:
        if bucket:
            for k, v in bucket:
                print k,v
