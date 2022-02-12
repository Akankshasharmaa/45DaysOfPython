"""Clock"""
class Clock:
    """Clock class"""
    def __init__(self, hour, minute):
        """input: hour and minute"""
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        """return: time as str"""
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        """return: time"""
        total_minutes = self.hour * 60 + self.minute
        new_hour = int(total_minutes // 60)
        new_minutes = int(total_minutes % 60)
        return f'{(new_hour % 24):0>2}:{(new_minutes % 60):0>2}'

    def __eq__(self, other):
        """equaling"""
        return str(self) == str(other)

    def __add__(self, minutes):
        """Adding minutes"""
        total_minutes = self.hour * 60 + self.minute + minutes
        self.hour = int(total_minutes // 60)
        self.minute = int(total_minutes % 60)
        return str(self)

    def __sub__(self, minutes):
        """Subtracting minutes"""
        total_minutes = self.hour * 60 + self.minute - minutes
        self.hour = int(total_minutes // 60)
        self.minute = int(total_minutes % 60)
        return str(self)
