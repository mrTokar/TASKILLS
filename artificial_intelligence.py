from get_any import get_hero_info, get_maps_info

class NeuronNetwork:
  def __init__(self, data: list):
    self.setting = data[0]
    self.location = data[1]
    self.mobs = data[2]
    self.items = data[3]


  def create_loc_info(self) -> str:
    """ЗАГЛУШКА\n
    Возращает весь текст из БД"""
    text = get_maps_info(self.location)
    return text


  def create_hero_info(self, mob: str) -> str:
    """ЗАГЛУШКА\n
    Возращает весь текст из БД"""
    text = get_hero_info(mob)
    return text

  def create_exposition(self) -> str:
    "Возращает готовый обработнный текст"
    exposition = self.create_loc_info() + "Здесь можно встретить разыных существ."
    for mob in self.mobs:
      mob_info = self.create_hero_info(mob)
      if mob_info is not None:
        exposition += " " + mob_info

    return exposition