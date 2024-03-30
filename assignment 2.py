class Artwork:
    def __init__(self, title, artist, creation_date, historical_significance, location, id_number):
        self.title = title
        self.artist = artist
        self.creation_date = creation_date
        self.historical_significance = historical_significance
        self.location = location
        self.id_number = id_number

    def display_info(self):
        return f"Title: {self.title}, Artist: {self.artist}, Created: {self.creation_date}, " \
               f"Historical Significance: {self.historical_significance}, Location: {self.location}, " \
               f"ID: {self.id_number}"

    def generate_exhibition_pass(self):
        # Simulate validation and pass generation
        print(f"Generating exhibition pass for: {self.title} by {self.artist}")
        pass_details = f"Artwork ID: {self.id_number}, Title: {self.title}, Location: {self.location}"
        # This is where the exhibition pass would be formatted and sent or printed
        print(f"Exhibition Pass Generated:\n{pass_details}")

# Example usage:
artwork = Artwork("Starry Night", "Vincent Van Gogh", "1889", "Impressionist masterpiece", "Gallery 1", "ART123")
artwork.generate_exhibition_pass()

class Visitor:
    def __init__(self, category, is_group=False, group_size=1):
        self.category = category  # e.g., 'adult', 'child', 'teacher', 'student', 'senior'
        self.is_group = is_group
        self.group_size = group_size if is_group else 1

class Ticket:
    def __init__(self, visitor, event_name, base_price=63):
        self.visitor = visitor
        self.event_name = event_name
        self.base_price = base_price
        self.final_price = self.calculate_final_price()

    def calculate_final_price(self):
        # Apply discounts based on visitor category or group status
        if self.visitor.category in ['child', 'teacher', 'student', 'senior']:
            return 0  # Free tickets for certain categories
        if self.visitor.is_group:
            price_after_discount = self.base_price * 0.5  # 50% discount for groups
        else:
            price_after_discount = self.base_price

        # Apply 5% VAT
        return price_after_discount * 1.05


class TicketingSystem:
    def purchase_ticket(self, visitor, event_name):
        # Special event pricing can be determined here and passed to Ticket
        ticket = Ticket(visitor, event_name)
        self.display_ticket_info(ticket)

    def display_ticket_info(self, ticket):
        print(f"Ticket for {ticket.event_name}:")
        print(f"Visitor Category: {ticket.visitor.category}")
        print(f"Group Purchase: {ticket.visitor.is_group}, Group Size: {ticket.visitor.group_size}")
        print(f"Final Price: {ticket.final_price:.2f} AED\n")

# Example usage
visitor_adult = Visitor('adult')
visitor_child = Visitor('child')
visitor_teacher = Visitor('teacher')
visitor_senior = Visitor('senior')
visitor_group = Visitor('adult', is_group=True, group_size=20)

system = TicketingSystem()
system.purchase_ticket(visitor_adult, "Regular Exhibition")
system.purchase_ticket(visitor_child, "Regular Exhibition")
system.purchase_ticket(visitor_teacher, "Science Fair")
system.purchase_ticket(visitor_senior, "Art Expo")
system.purchase_ticket(visitor_group, "Group Tour")






class Visitor:
    def __init__(self, name, category, email):
        self.name = name
        self.category = category  # e.g., 'adult', 'child', 'student', 'senior'
        self.email = email
        self.tickets = []

    def purchase_ticket(self, event, ticketing_system):
        ticket = ticketing_system.issue_ticket(self, event)
        if ticket:
            self.tickets.append(ticket)
            print(f"Ticket successfully purchased for {event.name} by {self.name}.")
        else:
            print("Unable to purchase ticket.")

class Event:
    def __init__(self, name, base_price, event_type='exhibition'):
        self.name = name
        self.base_price = base_price
        self.event_type = event_type  # 'exhibition', 'tour', 'special_event'

class Ticket:
    def __init__(self, visitor, event, price):
        self.visitor = visitor
        self.event = event
        self.price = price

    def display_ticket_info(self):
        return f"Ticket Info: Event: {self.event.name}, Visitor: {self.visitor.name}, Price: {self.price} AED"

class TicketingSystem:
    VAT_RATE = 0.05

    def issue_ticket(self, visitor, event):
        final_price = self.calculate_ticket_price(visitor, event)
        if final_price is not None:
            ticket = Ticket(visitor, event, final_price)
            return ticket
        return None

    def calculate_ticket_price(self, visitor, event):
        if visitor.category in ['child', 'student', 'senior']:
            return 0  # Free for certain categories
        price = event.base_price
        if visitor.category == 'group':
            price *= 0.5  # 50% discount for groups
        price += price * self.VAT_RATE  # Apply VAT
        return price

# Example usage
ticketing_system = TicketingSystem()
exhibition = Event("Van Gogh Alive", 63)
tour = Event("Historical Tour", 50, "tour")
special_event = Event("Night at the Museum", 120, "special_event")

visitor1 = Visitor("John Doe", "adult", "john@example.com")
visitor2 = Visitor("Jane Doe", "child", "jane@example.com")

visitor1.purchase_ticket(exhibition, ticketing_system)
visitor2.purchase_ticket(exhibition, ticketing_system)

for ticket in visitor1.tickets:
    print(ticket.display_ticket_info())



# Assume classes Artwork, Visitor, Ticket, Exhibition, and Event are defined as per previous guidance
