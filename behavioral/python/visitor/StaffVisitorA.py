from abc    import ABC, abstractmethod

class StaffVisitor(ABC):
    @abstractmethod
    def visit(self, staff) ->None:
        pass