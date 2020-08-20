#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    route = {}
    dest = "NONE"
    for i in range(length):
        route[i] = ''
    print("route: {}".format(route))
    print("route",route)
    for i in range(length):
        for ticket in tickets:
            if ticket.source == dest:
                print("Found {}".format(dest))
                route[i] = ticket.destination
                dest = ticket.destination
                break
    print(route)
    return route
