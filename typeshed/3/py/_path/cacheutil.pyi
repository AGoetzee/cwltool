from typing import Any

class BasicCache:
    maxentries: Any = ...
    prunenum: Any = ...
    def __init__(self, maxentries: int = ...) -> None: ...
    def clear(self) -> None: ...
    def delentry(self, key: Any, raising: bool = ...) -> None: ...
    def getorbuild(self, key: Any, builder: Any): ...

class BuildcostAccessCache(BasicCache): ...

class WeightedCountingEntry:
    weight: Any = ...
    def __init__(self, value: Any, oneweight: Any) -> None: ...
    def value(self): ...
    value: Any = ...

class AgingCache(BasicCache):
    maxseconds: Any = ...
    def __init__(self, maxentries: int = ..., maxseconds: float = ...) -> None: ...

class AgingEntry:
    value: Any = ...
    weight: Any = ...
    def __init__(self, value: Any, expirationtime: Any) -> None: ...
    def isexpired(self): ...