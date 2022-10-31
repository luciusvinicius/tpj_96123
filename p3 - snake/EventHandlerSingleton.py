from EventHandler import EventHandler


class EventHandlerSingleton():
    __instance = None
    
    def __init__(self):
        if EventHandlerSingleton.__instance is None:
            EventHandlerSingleton.__instance = EventHandler()
        
    def get(self):
        return EventHandlerSingleton.__instance