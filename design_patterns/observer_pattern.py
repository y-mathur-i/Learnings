"""Module to examplify observer design pattern
"""
from enum import Enum
from abc import ABCMeta, abstractmethod
from typing import Any


class Event(Enum):
    """Types on events supported by the NewsBroadcaster
    """
    SPORTS = "sports"
    WEATHER = "weather"
    BREAKING_NEWS = "breaking_news"


class Observer(metaclass=ABCMeta):
    """Interfacxe to be implemented by every observer
    """
    observer_type: Event
    @abstractmethod
    def update(self, data: Any):
        """Method to be implemented for every observer
        """


class NewsBroadcaster:
    """Main class with data that registers and notifies the observers
    """
    def __init__(self) -> None:
        self.observers = {event: [] for event in Event}
        self.data_mapping = {Event.SPORTS: "N/A",
                             Event.WEATHER: {"Temp": "N/A", "humidity": "N/A"},
                             Event.BREAKING_NEWS: None}

    def register_observer(self, observer: Observer) -> None:
        """Method to register observer
        """
        self.observers[observer.observer_type].append(observer)

    def update(self, event_type: Event, data) -> None:
        """Method to update the data based on event type
            SHOULD ALSO INCLUDE SOME TYPE OF VALIDATION
            CAN BE DONE BY PYDANTIC
        """
        self.data_mapping[event_type] = data
        self.notify(event_type)

    def notify(self, event_type: Event) -> None:
        """Method to notify observers
        """
        for observer in self.observers[event_type]:
            observer.update(self.data_mapping[event_type])

class SportNews(Observer):
    """Observer to deal with sports news
    """
    observer_type = Event.SPORTS
    def __init__(self) -> None:
        super().__init__()
        self.current_sports_headline = None

    def update(self, data: Any):
        self.current_sports_headline = data


class WeatherBoard(Observer):
    """Observer to deal with weather news
    """
    observer_type = Event.WEATHER
    def __init__(self) -> None:
        super().__init__()
        self.weather_data = {"Temp": "N/A", "humidity": "N/A"} 

    def update(self, data: Any):
        self.weather_data = data

if __name__=="__main__":
    broadcaster = NewsBroadcaster()
    sports_news_observer = SportNews()
    broadcaster.register_observer(sports_news_observer)
    weather_board = WeatherBoard()
    broadcaster.register_observer(weather_board)
    print(f"Data in sports news before: {sports_news_observer.current_sports_headline}")
    print("Updating sports data for the news broadcaster")
    broadcaster.update(Event.SPORTS, "THE CUP COMES HOME!!!!!!")
    print(f"Data in sports news after: {sports_news_observer.current_sports_headline}")
    # same way others observers can be onboarded
