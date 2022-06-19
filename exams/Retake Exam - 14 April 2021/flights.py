def flights(*args):
    result = {}
    flights_data = args[:args.index("Finish")]
    flights_destination = [el for i, el in enumerate(flights_data) if i % 2 == 0]
    flights_passengers = [el for i, el in enumerate(flights_data) if i % 2 != 0]
    for count, flight in zip(flights_passengers, flights_destination):
        if flight not in result:
            result[flight] = 0
        result[flight] += count
    return result

print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))

