broker_url = 'redis://localhost:6379/'
result_backend = 'redis://localhost:6379/'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Asia/Bishkek'
enable_utc = False
broker_connection_retry_on_startup = True