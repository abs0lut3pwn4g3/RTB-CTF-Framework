import os

from flask_caching import Cache

cache_redis_url = os.environ.get("REDIS_URL", None)

if not cache_redis_url:
    config = {"CACHE_TYPE": "simple"}
else:
    config = {"CACHE_TYPE": "redis", "CACHE_REDIS_URL": cache_redis_url}


cache = Cache(config=config)
