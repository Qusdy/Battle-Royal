from cut_title_sheet import cut_title_sheet
from load_image import load_image
from base_crystal import BaseCrystal


class Emerald(BaseCrystal):
    def __init__(self, pos, *group):
        self.image = cut_title_sheet(load_image("resources_basic.png"), 11, 11, 2, 2)
        super().__init__(pos, *group)
        self.spell = 'ice_dart'
