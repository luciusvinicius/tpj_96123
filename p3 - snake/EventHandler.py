class EventHandler():
    def __init__(self):
        self.events = []
    
    def registry(self, event):
        self.events.append(event)
    
    def notify(self, event_name, *args):
        for event in self.events:
            event.listen(event_name, args)