from abc import ABC, abstractmethod
from typing import Dict
class DatabaseRespositoryInterface(ABC):
  
  @abstractmethod
  def insert_artist(self, data: Dict) -> None:
    pass