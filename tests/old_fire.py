#!/usr/bin/env python
#
# An engine for JML files
# Copyright (C) 2022
# Birbone Productions
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

def __main__(x):
    """Fire Engine"""
    key = []
    value = ()
    dic = ()
    # Take the keys
    for i, line in enumerate(x):
        if line[0] == '[':
            keyName= ""
            tmp_value = ""
            key1 = line.find('[')+1
            key2 = line.find(']')
            keyName = line[key1:key2]
            if not(search_used_key(keyName, key)):
                key.append(keyName)
            else:
                raise DuplicateKeyError(f"Duplicate key for {keyName}")
            tmp_value = line[key2+1:len(line)-1]
            if(tmp_value.isnumeric()):
                value += (int(tmp_value),)
            else:
                #Boolean
                if not ("\"" in tmp_value):
                    if(tmp_value == "True"):
                        value += (True,)
                    elif(tmp_value == "False"):
                        value += (False,)
                    else:
                        raise NumberError("Error in list. Misunderstanding type.")
                #List
                elif("|" in line):
                    l = line[key2+1:len(line)-1].split("|")
                    temp_vlist = []
                    isString = False
                    for i in l:
                        if("\"" in i):
                            isString = True
                            temp_vlist.append(i.replace("\"", ""))
                        else:
                            if not (isString):
                                if(i.isnumeric()):
                                    temp_vlist.append(int(i))
                                else:
                                    raise NumberError("Error in list. Misunderstanding type.")
                            else:
                                if(i=="True"):
                                    temp_vlist.append(True)
                                elif(i=="False"):
                                    temp_vlist.append(False)
                                else:
                                    raise NumberError("Error in tuple. Misunderstanding type.")
                    value += (temp_vlist,)
                #Tuple
                elif("/" in line):
                    l = line[key2+1:len(line)-1].split("/")
                    temp_vtuple = ()
                    for i in l:
                        if("\"" in i):
                            temp_vtuple = temp_vtuple + (i.replace("\"", ""),)
                        else:
                                if(i.isnumeric()):
                                    temp_vtuple = temp_vtuple + (int(i),)
                                else:
                                    if(i=="True"):
                                        temp_vtuple = temp_vtuple + (True,)
                                    elif(i=="False"):
                                        temp_vtuple = temp_vtuple + (False,)
                                    else:
                                        raise NumberError("Error in tuple. Misunderstanding type.")
                    value += (temp_vtuple,)
                #String
                else:
                    tmp_value = tmp_value.replace("\"", "")
                    value += (tmp_value,)

    dic = dic + (key,value)
    return dic

def search_used_key(key, list):
    if(key in list):
        return True
    else:
        return False


class StringError(Exception):
    pass
class SpaceBetween(Exception):
    pass
class NumberError(Exception):
    pass
class DuplicateKeyError(Exception):
    pass


f = open("testFile.jml", "r")

print(__main__(f))

