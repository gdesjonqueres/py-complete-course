from typing import List


class Segment:
    def __init__(self, departure, destination):
        self.departure = departure
        self.destination = destination


class Flight:
    def __init__(self, segments: List[Segment]):
        self.segments = segments

    def __repr__(self):
        """
        :return: string in the format of `GLA -> LHR -> TOR`
        """
        # seg_str = ''
        # for seg in self.segments:
        #     seg_str += seg.departure + ' -> '
        # seg_str += self.segments[-1].destination

        # return f'<Flight {seg_str}>'

        stops = [self.segments[0].departure, self.segments[0].destination]
        for segment in self.segments[1:]:
            stops.append(segment.destination)

        return ' -> '.join(stops)

    @property
    def departure_point(self) -> str:
        return self.segments[0].departure

    @departure_point.setter
    def departure_point(self, new_departure):
        destination = self.segments[0].destination
        self.segments[0] = Segment(departure=new_departure, destination=destination)


flight = Flight([Segment('GLA', 'LHR'), Segment('LHR', 'TOR')])
print(flight.departure_point)

flight.departure_point = 'EDI'
print(flight.departure_point)

print(flight)
