from plyer import notification

# Create a notification
notification.notify(
    title="Reminder",
    message="Time to take a break and stretch!",
    app_name="Notifier",
    timeout=10  # Display for 10 seconds
)
