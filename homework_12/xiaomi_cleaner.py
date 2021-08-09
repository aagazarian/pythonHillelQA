from vacuum_cleaner import VacuumCleaner


class XiaomiCleaner(VacuumCleaner):
    def __init__(self, model_name: str, power: float, battery_capacity: float):
        super().__init__(model_name, power, battery_capacity)
        self.__remaining_work_hour = None
        print(model_name, power, battery_capacity, self.__remaining_work_hour)

    def _updated_remaining_work_time(self):
        self.__remaining_work_hour = (9 * self._battery_capacity) / self._power

    def _update_batter_capacity(self, minutes):
        hours = minutes / 60
        used_capacity = self._power * hours / (9 * 0.9)
        print(f"used capacity for {minutes} min is: {used_capacity}")
        self._battery_capacity -= used_capacity

    def vacuum(self, minutes: int):
        self._updated_remaining_work_time()
        print(f"I'm Xiaomi. Checking battery status")
        print(
            f"Remaining working time in minutes before clean: {self.__remaining_work_hour * 60}"
        )

        if minutes >= self.__remaining_work_hour * 60:
            raise Exception("Not possible to clean more than capacity")
        else:
            print("I start clean")
            self._update_batter_capacity(minutes)
            self._updated_remaining_work_time()
            print(f"I'm done")
        print(
            f"Remaining working time in minutes after clean: {self.__remaining_work_hour * 60}"
        )
