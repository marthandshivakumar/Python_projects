class Event:
    def __init__(self, event_id, name, date, location, ticket_price, max_capacity):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.location = location
        self.ticket_price = ticket_price
        self.max_capacity = max_capacity
        self.attendees = []

    def add_attendee(self, attendee):
        self.attendees.append(attendee)

    def ticket_sold(self, attendee):
        if len(self.attendees) < self.max_capacity:
            self.add_attendee(attendee)
            return True
        else:
            return False

    def attendee_count(self):
        return len(self.attendees)

    def remaining_capacity(self):
        return self.max_capacity - len(self.attendees)


class Attendee:
    def __init__(self, attendee_id, name, email):
        self.attendee_id = attendee_id
        self.name = name
        self.email = email
        self.ticket_id = None
        self.event_id = None

    def register_event(self, event_id):
        self.event_id = event_id

    def purchase_ticket(self, ticket_id):
        self.ticket_id = ticket_id

    def view_event_details(self, events):
        for event in events:
            if event.event_id == self.event_id:
                return f"Event Name: {event.name}\nDate: {event.date}\nLocation: {event.location}\nTicket Price: {event.ticket_price}"


def main_menu():
    print("\nEvent Management System Menu:")
    print("1. Add Event")
    print("2. Register Attendee")
    print("3. Purchase Ticket")
    print("4. View Attendee List for Event")
    print("5. View Event Details")
    print("6. Exit")


def add_event(events):
    event_id = len(events) + 1
    name = input("Enter event name: ")
    date = input("Enter event date: ")
    location = input("Enter event location: ")
    ticket_price = float(input("Enter ticket price: "))
    max_capacity = int(input("Enter maximum capacity: "))
    event = Event(event_id, name, date, location, ticket_price, max_capacity)
    events.append(event)
    print(f"Event '{name}' added successfully with ID {event_id}")


def register_attendee(attendees):
    attendee_id = len(attendees) + 1
    name = input("Enter attendee name: ")
    email = input("Enter attendee email: ")
    attendee = Attendee(attendee_id, name, email)
    attendees.append(attendee)
    print(f"Attendee '{name}' registered successfully with ID {attendee_id}")


def purchase_ticket(events, attendees):
    event_id = int(input("Enter event ID: "))
    for event in events:
        if event.event_id == event_id:
            if event.ticket_sold(attendees[-1]):
                attendees[-1].register_event(event_id)
                attendees[-1].purchase_ticket(len(event.attendees))
                print(f"Ticket purchased successfully for event '{event.name}'")
            else:
                print(f"Event '{event.name}' is already full!")
            return
    print(f"Event with ID {event_id} not found.")


def view_attendee_list(events, attendees):
    event_id = int(input("Enter event ID: "))
    for event in events:
        if event.event_id == event_id:
            print(f"\nAttendee List for Event '{event.name}':")
            for attendee in event.attendees:
                print(f"Attendee ID: {attendee.attendee_id}, Name: {attendee.name}")
            return
    print(f"Event with ID {event_id} not found.")


def view_event_details(events):
    print("\nEvent Details:")
    for event in events:
        print(f"Event ID: {event.event_id}, Name: {event.name}, Date: {event.date}, Location: {event.location}, Ticket Price: {event.ticket_price}")


# Main program
events = []
attendees = []

while True:
    main_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_event(events)
    elif choice == '2':
        register_attendee(attendees)
    elif choice == '3':
        purchase_ticket(events, attendees)
    elif choice == '4':
        view_attendee_list(events, attendees)
    elif choice == '5':
        view_event_details(events)
    elif choice == '6':
        print("Exiting Event Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
