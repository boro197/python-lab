from abc import ABC, abstractmethod


class Component:
    def __init__(self, price, description):
        super().__init__()
        self._price = price
        self._description = description
        self._components = []

    @property
    def price(self):
        price = self._price
        for component in self._components:
            price = price + component.price
        return price

    @property
    def description(self):
        return "* {0} ({1} PLN)".format(self._description, self.price)

    def add_component(self, component):
        self._components.append(component)

    def print_description(self, level=1):
        print("\t" * level + self.description)
        for component in self._components: 
            component.print_description(level + 1)
