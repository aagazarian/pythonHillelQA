from abc import ABC, abstractmethod


class VacuumCleaner(ABC):
    def __init__(self,
                 model_name: str,
                 power: float,
                 battery_capacity: float,
                 remaining_work_time: float
                 ):
        self._model_name = model_name
        self._power = power
        self._battery_capacity = battery_capacity
        self._remaining_work_time = remaining_work_time

    @abstractmethod
    def vacuum(self, minutes: int):
        pass

    @abstractmethod
    def _updated_remaining_work_time(self):
        pass

    @abstractmethod
    def _update_batter_capacity(self):
        pass
