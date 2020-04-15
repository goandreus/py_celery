*****
REDBEAT TO CELERY
*****

Redisbeat is a Celery Beat Scheduler that stores periodic tasks and their status in a Redis Datastore.

CELERY CONFIG
####

REDBEAT_REDIS_URL = getvar('REDBEAT_REDIS_URL', 'redis://localhost:6379/1')
REDBEAT_REDIS_OPTIONS = {
    'retry_period': 60,
}
REDBEAT_KEY_PREFIX = 'redisbeat'


