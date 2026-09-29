"""
Topic: Factory Pattern
A factory centralizes object creation logic, so calling code doesn't need to
know which concrete class to instantiate - useful when creation logic is
complex or depends on runtime input.
"""

from abc import ABC, abstractmethod


# --- 1. The Product Hierarchy ---
class Notification(ABC):
    """Common interface that every concrete notification type must implement."""

    @abstractmethod
    def send(self, message):
        raise NotImplementedError


class EmailNotification(Notification):
    def send(self, message):
        return f"Sending EMAIL: '{message}'"


class SMSNotification(Notification):
    def send(self, message):
        return f"Sending SMS: '{message}'"


class PushNotification(Notification):
    def send(self, message):
        return f"Sending PUSH notification: '{message}'"


# --- 2. The Factory Function ---
# Centralizes the "which class do I create?" decision in a single place.
def create_notification(kind):
    """Return the appropriate Notification subclass instance for 'kind'."""
    notification_types = {
        "email": EmailNotification,
        "sms": SMSNotification,
        "push": PushNotification,
    }
    notification_class = notification_types.get(kind)
    if notification_class is None:
        raise ValueError(f"Unknown notification kind: {kind!r}")
    return notification_class()


print("--- Factory Pattern ---")
for kind in ["email", "sms", "push"]:
    notifier = create_notification(kind)
    print(notifier.send("Your order has shipped!"))


# --- 3. Why This Helps: Adding a New Type Doesn't Touch Calling Code ---
print("\n--- Extending the Factory ---")


class SlackNotification(Notification):
    def send(self, message):
        return f"Sending SLACK message: '{message}'"


def create_notification_v2(kind):
    """An updated factory - callers still just say 'give me a notifier'."""
    notification_types = {
        "email": EmailNotification,
        "sms": SMSNotification,
        "push": PushNotification,
        "slack": SlackNotification,
    }
    notification_class = notification_types.get(kind)
    if notification_class is None:
        raise ValueError(f"Unknown notification kind: {kind!r}")
    return notification_class()


slack_notifier = create_notification_v2("slack")
print(slack_notifier.send("Deployment finished."))

try:
    create_notification_v2("carrier-pigeon")
except ValueError as error:
    print(f"Invalid kind handled gracefully: {error}")
