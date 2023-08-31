"""Stub file for spacer.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Union, overload, Optional
from reflex.components.libs.chakra import ChakraComponent
from reflex.components.component import Component
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain

class Spacer(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "Spacer": ...  # type: ignore