#!/usr/bin/env python
#
# An engine for JML files
# Copyright (C) 2022
# Jonio Computer
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
import fire
from prettytable import PrettyTable
def _display(x):
    fire_tuple = fire.__main__(x)
    for i, item in enumerate(fire_tuple[0]):
        if not(item.lower()=="none"):
            print(f"{item}: {fire_tuple[1][i]}")

def _display_table(x):
    fire_tuple = fire.__main__(x)
    columns = []
    for i in fire_tuple[0]:
        columns.append(i)
    t = PrettyTable(columns)
    for i, item in enumerate(fire_tuple[1]):
        t.add_column(fire_tuple[0][i], [item])
    print(t)

def _display_raw(x):
    print(fire.__main__(x))

f = open("../tests/testFile.jml", "r")
print(_display_raw(f))