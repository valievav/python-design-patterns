class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data


class UnknownEvent(Event):
    """A type of event that cannot be identified from its data."""


class LoginEvent(Event):
    """A event representing a user that has just entered the system."""


class LogoutEvent(Event):
    """An event representing a user that has just left the system."""


class SystemMonitor:
    """Identify events that occurred in the system."""
    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        if self.event_data["before"]["session"] == 0 and self.event_data["after"]["session"] == 1:
            return LoginEvent(self.event_data)
        elif self.event_data["before"]["session"] == 1 and self.event_data["after"]["session"] == 0:
            return LogoutEvent(self.event_data)
        else:
            return UnknownEvent(self.event_data)

    # each time new condition appears - if else list will grow and it will require SystemMonitor modification


if __name__ == "__main__":
    data = {"before": {"session": 0}, "after": {"session": 1}}
    monitor = SystemMonitor(data)
    print(monitor.identify_event().__class__.__name__)

    assert SystemMonitor({"before": {"session": 0}, "after": {"session": 1}}).identify_event().__class__.__name__ == "LoginEvent"
    assert SystemMonitor({"before": {"session": 1}, "after": {"session": 0}}).identify_event().__class__.__name__ == "LogoutEvent"
    assert SystemMonitor({"before": {"session": None}, "after": {"session": None}}).identify_event().__class__.__name__ == "UnknownEvent"
