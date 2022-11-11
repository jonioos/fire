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
import fire_exceptions as ex
def __main__(x):
    """Fire Engine"""
    key = []
    group_appartenance_key = []
    value = ()
    dic = ()
    group_key = []
    group = ()
    isGroup = False
    # Take the keys
    for i, line in enumerate(x):
        if line[0] == '(':
                first_char = line.find('(')+1
                end_char = line.find(')')
                group_name = line[first_char:end_char]
                if not(group_name == "ENDGROUP"):
                    if not(search_used_key(group_name, group_key)):
                        group_key.append(group_name)
                        isGroup = True
                    else:
                        raise ex.DuplicateKeyError(f"Duplicate group key for ({group_name}) in line {i+1}")

        if line[0] == '[':
            keyName= ""
            tmp_value = ""
            key1 = line.find('[')+1
            key2 = line.find(']')
            keyName = line[key1:key2]
            if not isGroup:
                if not(search_used_key(keyName, key)):
                    key.append(keyName)
                else:
                    raise ex.DuplicateKeyError(f"Duplicate key for [{keyName}]")
            else:
                for i, item in enumerate(key):
                    if group_appartenance_key[i] == group_name and keyName == item:
                        raise ex.DuplicateKeyError(f"Duplicate key for [{keyName}] inside group ({group_name})")
                key.append(keyName)
                group_appartenance_key.append(group_name)


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
                        raise ex.SyntaxError(f"Misunderstanding type in line {str(i+1)}")
                #List
                elif("|" in line):
                    l = line[key2+1:len(line)-1].split("|")
                    temp_vlist = []
                    isString = False
                    for item in l:
                        if("\"" in item):
                            isString = True
                            temp_vlist.append(item.replace("\"", ""))
                        else:
                            if not (isString):
                                if(i.isnumeric()):
                                    temp_vlist.append(int(item))
                                else:
                                    raise ex.SyntaxError(f"Error in list. Misunderstanding type in line {str(i+1)}")
                            else:
                                if(item=="True"):
                                    temp_vlist.append(True)
                                elif(item=="False"):
                                    temp_vlist.append(False)
                                else:
                                    raise ex.SyntaxError(f"Error in list. Misunderstanding type in line {str(i+1)}")
                    value += (temp_vlist,)
                #Tuple
                elif("/" in line):
                    l = line[key2+1:len(line)-1].split("/")
                    temp_vtuple = ()
                    for item in l:
                        if("\"" in item):
                            temp_vtuple = temp_vtuple + (item.replace("\"", ""),)
                        else:
                                if(item.isnumeric()):
                                    temp_vtuple = temp_vtuple + (int(item),)
                                else:
                                    if(item=="True"):
                                        temp_vtuple = temp_vtuple + (True,)
                                    elif(item=="False"):
                                        temp_vtuple = temp_vtuple + (False,)
                                    else:
                                        raise ex.NumberError(f"Error in tuple. Misunderstanding type in line {i+1}")
                    value += (temp_vtuple,)
                #String
                else:
                    tmp_value = tmp_value.replace("\"", "")
                    value += (tmp_value,)
        elif(line[0] == "("):
            pass
        else:
            raise ex.SyntaxError(f"Syntax error in line {str(i+1)}")

    dic = dic + (key,value)
    if(isGroup == True):
        group = group + (group_key, dic)
        return group
    else:
        return dic

def search_used_key(key, list):
    if(key in list):
        return True
    else:
        return False






