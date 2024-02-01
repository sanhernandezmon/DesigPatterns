from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

# Element interface
class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass

# Concrete Element
class ConcreteElementA(Element):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_concrete_element_a(self)

# Concrete Element
class ConcreteElementB(Element):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_concrete_element_b(self)

# Visitor interface
class Visitor(ABC):
    @abstractmethod
    def visit_concrete_element_a(self, element: ConcreteElementA) -> None:
        pass

    @abstractmethod
    def visit_concrete_element_b(self, element: ConcreteElementB) -> None:
        pass

# Concrete Visitor
class ConcreteVisitor(Visitor):
    def visit_concrete_element_a(self, element: ConcreteElementA) -> None:
        print("Visitor is processing ConcreteElementA")

    def visit_concrete_element_b(self, element: ConcreteElementB) -> None:
        print("Visitor is processing ConcreteElementB")

# Object Structure
class ObjectStructure:
    def __init__(self):
        self.elements: List[Element] = []

    def attach(self, element: Element) -> None:
        self.elements.append(element)

    def detach(self, element: Element) -> None:
        self.elements.remove(element)

    def accept(self, visitor: Visitor) -> None:
        for element in self.elements:
            element.accept(visitor)


element_a = ConcreteElementA()
element_b = ConcreteElementB()

object_structure = ObjectStructure()

object_structure.attach(element_b)
object_structure.attach(element_a)

visitor = ConcreteVisitor()

object_structure.accept(visitor)
