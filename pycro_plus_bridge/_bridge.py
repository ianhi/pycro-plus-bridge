from pycromanager import Core as pycroCore
from pymmcore_plus import CMMCorePlus

__all__ = [
    "pycroCorePlus",
]

# typing taken from pymmcore-plus
from typing import List, Tuple, TypeVar, Union

_T = TypeVar("_T")

ListOrTuple = Union[List[_T], Tuple[_T, ...]]


class pycroCorePlus(pycroCore, CMMCorePlus):
    def __init__(self, mm_path=None, adapter_paths: ListOrTuple[str] = None):
        pycroCore().__init__()
        CMMCorePlus().__init__(mm_path, adapter_paths)
        # TODO 1: convert pycromanager signals to work with self.events
        # TODO 2: register pycromanager acquisition engine as an mda engine
