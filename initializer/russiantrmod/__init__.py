import renpy
import renpy.ast as ast

from modloader import modinfo
from modloader.modclass import Mod, loadable_mod



@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return ("Russian Translation Demo", "v1", "Wolfniey")

    def mod_load(self):
        pass

    def mod_complete(self):
        pass
