class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    @staticmethod  # method that all child methods can overload with unique condition
    def meets_condition(event_data: dict):
        pass


class UnknownEvent(Event):
    """A type of event that cannot be identified from its data."""


class LoginEvent(Event):
    """A event representing a user that has just entered the system."""
    def meets_condition(event_data: dict):
        return event_data["before"]["session"] == 0 and event_data["after"]["session"] == 1


class LogoutEvent(Event):
    """An event representing a user that has just left the system."""
    def meets_condition(event_data: dict):
        return event_data["before"]["session"] == 1 and event_data["after"]["session"] == 0


class SystemMonitor:
    """Identify events that occurred in the system."""
    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        for event_cls in Event.__subclasses__():
            try:
                if event_cls.meets_condition(self.event_data):
                    return event_cls(self.event_data)
            except KeyError:
                continue

        return UnknownEvent(self.event_data)

# when new Even type appears, no modification to SystemMonitor will be done,
# only new EventType will be created that's inherits from Event with unique meets_condition


if __name__ == "__main__":
    data = {"before": {"session": 0}, "after": {"session": 1}}
    monitor = SystemMonitor(data)
    print(monitor.identify_event().__class__.__name__)

    assert SystemMonitor({"before": {"session": 0}, "after": {"session": 1}}).identify_event().__class__.__name__ == "LoginEvent"
    assert SystemMonitor({"before": {"session": 1}, "after": {"session": 0}}).identify_event().__class__.__name__ == "LogoutEvent"
    assert SystemMonitor({"before": {"session": None}, "after": {"session": None}}).identify_event().__class__.__name__ == "UnknownEvent"
