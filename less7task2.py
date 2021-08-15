#задание №2
from abc import ABC, abstractmethod

class Odejda (ABC):
  def __init__(self, nazvanie):
    self.nazvanie = nazvanie
  @abstractmethod
  def kol_mat (self):
    pass


class Palto(Odejda):
  def __init__(self, razmer):
    self.razmer = razmer
  @property
  def kol_mat (self):
    return self.razmer/6.5 + 0.5

class Kostum(Odejda):
  def __init__(self, rost):
    self.rost = rost
  @property
  def kol_mat (self):
    return self.rost*2 + 0.3

palto_1 = Palto (49)
kostum_1 = Kostum (1.80)

print(palto_1.kol_mat)
print(kostum_1.kol_mat)























