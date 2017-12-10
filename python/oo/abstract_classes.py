"""A class that has a metaclass derived from ABCMeta cannot be
instantiated unless all of its abstract methods and properties
are overridden."""

from abc import ABC, abstractmethod


class Abstract(ABC):
    """Trying to instantiate this class will raise the next exception
    'TypeError: Can't instantiate abstract class Abstract with abstract
    methods do_something'"""
    @abstractmethod
    def do_something(self):
        print("I can't do anything!")


class Concrete(Abstract):
    def do_something(self):
        print("I'm doing something!")


class OldWayAbstract(object):
    """The weakness of this approach is that the user can instantiate
    this class, and won't see the exception until the method is called
    at runtime."""
    def do_something(self):
        raise NotImplementedError('subclasses must override foo()!')


class OldWayDerived(OldWayAbstract):
    def do_something(self):
        print("Hooray!")


if __name__ == "__main__":
    c = Concrete()
    c.do_something()

    o = OldWayDerived()
    o.do_something()
