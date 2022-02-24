from celery.schedules import crontab
import celery


broker_url = "redis://localhost:6379/0"
result_backend = "redis://localhost:6379/0"
send_sent_event = True
timezone = "Europe/Lisbon"
imports = "git_automate.end"
task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]
beat_schedule = {
    "git_timetable": {
        "task": "main.start",
        "schedule": crontab(minute="*/1"),
        "args": (),
    },
}
