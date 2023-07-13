from battery import Battery
from util import add_years_to_date


class NubbinBattery(Battery):
    def __int__(self, current_date, last_serviced_date):
        self.current_date = current_date
        self.last_serviced_date = last_serviced_date

    def needs_service(self):
        date_when_to_service = add_years_to_date(self.last_serviced_date, 4)
        if date_when_to_service < self.current_date:
            return True
        else:
            return False
