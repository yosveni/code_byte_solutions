#!/bin/python3

import math
import os
import random
import re
import sys


class Multiset:

    def __init__(self):
        self.multiset = []
    def add(self, val):
        self.multiset.append(val)

    def remove(self, val):
        if val in self.multiset:
           self.multiset.remove(val)

    def __contains__(self, val):
        return val in self.multiset

    def __len__(self):
        return len(self.multiset)

