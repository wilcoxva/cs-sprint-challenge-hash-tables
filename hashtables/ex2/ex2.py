#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    route = list(range(length))
    flight_matrix = dict()
    for ticket in tickets:
        flight_matrix.update({ticket.source: ticket.destination})
    
    src = "NONE"
    for i in range(length):
        route[i] = flight_matrix[src]
        src = flight_matrix[src]
    return route 