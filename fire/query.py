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
import fire_exceptions as ex
import re

def main():
    _global_file = ""
    _global_tuple = ()
    _command_history = []
    print("FIRE Engine for Jonio Markup Language, (C)Jonio Computer")
    print("Load a JML file with the command \"load filename.jml\"")
    while not False:
        comando = input("FIRE:> ")
        c = comando.split(' ')
        try:
            _command_history.append(c)
            if(c[0] == "load"):
                _global_file = open("../tests/testFile.jml", "r")
                _global_tuple = fire.__main__(_global_file)

            if(c[0] == "export"):
                if(_global_file == ""):
                    raise ex.JMLNotFound("JML not found. First load a JML file.")
                if len(c) >= 1:
                    #A gruppi
                    #fare il print nel nome del gruppo
                    _my_group = ""
                    if(c[1] in str(_global_tuple)):
                        local_tuple = list(_global_tuple)

                        for item in _global_tuple[0]:
                            print(item)

                        for i, item in enumerate(local_tuple[1][0]):
                            if(item == c[1]):
                                print(f"{local_tuple[1][1][i]}")

        except Exception as e:
            print("[ERROR]: " + str(e))

def _select_key(key):
    temp_table=()

main()