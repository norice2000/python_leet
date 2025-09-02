class EventBuffer:
    def append_event(self, event_data):
        new_event = Event(event_data)

        self.tail.next = new_event
        new_event.prev = self.tail
        self.tail = self.tail.next