from scramblers.affine_transformation import AffineTransformation
from scramblers.key_word import KeyWord
from scramblers.railway_hedge import RailwayHedge
from scramblers.scramblers_master import ScramblersMaster
from scramblers.upper_by_blocks import UpperByBlocks
from scramblers.upper_reversed import UpperReversed
from scramblers.upper_without_spaces import UpperWithoutSpaces

scramblers = [
    UpperReversed(),
    UpperByBlocks(),
    UpperWithoutSpaces(),
    RailwayHedge(),
    KeyWord(),
    AffineTransformation()
]

scramblers_master = ScramblersMaster(scramblers)
text = "Прокопенко Артур Романович"
print(scramblers_master.process_all(text))
