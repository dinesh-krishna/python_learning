"""
Topic: Observer Pattern
Lets one object (the "subject") notify a list of dependent objects
("observers") automatically whenever its state changes, without the subject
needing to know any details about them.
"""


# --- 1. The Subject: Something Worth Watching ---
class WeatherStation:
    """Publishes temperature updates to any number of subscribed observers."""

    def __init__(self):
        self._observers = []
        self._temperature = None

    def subscribe(self, observer):
        """Register an observer to be notified of future changes."""
        self._observers.append(observer)

    def unsubscribe(self, observer):
        """Stop notifying a previously subscribed observer."""
        self._observers.remove(observer)

    def set_temperature(self, temperature):
        """Update the state and notify every subscribed observer."""
        print(f"\nWeatherStation: temperature changed to {temperature}°C")
        self._temperature = temperature
        for observer in self._observers:
            observer.update(self._temperature)


# --- 2. Observers: React to Notifications, Each in Their Own Way ---
class DisplayPanel:
    """One kind of observer: shows the temperature on a display."""

    def __init__(self, name):
        self.name = name

    def update(self, temperature):
        print(f"  [{self.name}] Display now shows: {temperature}°C")


class FreezeAlarm:
    """Another kind of observer: only reacts when it matters to it."""

    def update(self, temperature):
        if temperature <= 0:
            print(f"  [FreezeAlarm] WARNING: Freezing temperature detected ({temperature}°C)!")


print("--- Observer Pattern ---")
station = WeatherStation()
lobby_display = DisplayPanel("Lobby")
office_display = DisplayPanel("Office")
freeze_alarm = FreezeAlarm()

station.subscribe(lobby_display)
station.subscribe(office_display)
station.subscribe(freeze_alarm)

station.set_temperature(22)
station.set_temperature(-3)

# --- 3. Observers Can Unsubscribe at Any Time ---
print("\n--- Unsubscribing an Observer ---")
station.unsubscribe(office_display)
station.set_temperature(18)
