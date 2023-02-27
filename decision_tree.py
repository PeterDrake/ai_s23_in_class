ATTRIBUTES = ('Alternative', 'Bar', 'Friday/Saturday', 'Hungry', 'Patrons', 'Price', 'Raining',
              'Reservation', 'Type', 'Wait')


class Datum:
    def __init__(self, target, *values):
        self.target = target
        self.attributes = dict(zip(ATTRIBUTES, values))


data = (Datum(True, True, False, False, True, 'Some', '$$$', False, True, 'French', '0-10'),
        Datum(False, True, False, False, True, 'Full', '$', False, False, 'Thai', '30-60'),
        Datum(True, False, True, False, False, 'Some', '$', False, False, 'Burger', '0-10'),
        Datum(True, True, False, True, True, 'Full', '$', True, False, 'Thai', '10-30'),
        Datum(False, True, False, True, False, 'Full', '$$$', False, True, 'French', '>60'),
        Datum(True, False, True, False, True, 'Some', '$$', True, True, 'Italian', '0-10'),
        Datum(False, False, True, False, False, 'None', '$', True, False, 'Burger', '0-10'),
        Datum(True, False, False, False, True, 'Some', '$$', True, True, 'Thai', '0-10'),
        Datum(False, False, True, True, False, 'Full', '$', True, False, 'Burger', '>60'),
        Datum(False, True, True, True, True, 'Full', '$$$', False, True, 'Italian', '10-30'),
        Datum(False, False, False, False, False, 'None', '$', False, False, 'Thai', '0-10'),
        Datum(True, True, True, True, True, 'Full', '$', False, False, 'Burger', '30-60'))
