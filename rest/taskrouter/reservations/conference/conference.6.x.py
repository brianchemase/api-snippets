# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"
workspace_sid = "WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
task_sid = "WTXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
reservation_sid = "WRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

client = Client(account_sid, auth_token)

#  Update a Reservation with a Conference instruction
reservation = client.taskrouter.workspaces(workspace_sid) \
    .tasks(task_sid).reservations(reservation_sid) \
    .update(
        instruction='conference',
        from_='+18001231234',
        conference_status_callback='https://www.example.com/ConferenceEvents',
        conference_status_callback_event=["start", "end", "join", "leave", "mute", "hold"]
    )

print(reservation.reservation_status)
print(reservation.worker_name)
