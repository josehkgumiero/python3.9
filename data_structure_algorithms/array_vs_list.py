# python ./data_structure_algorithms/array_vs_list.py

import numpy as np

import pprint

import copy

_array = np.array([1, 2, 3, 4, 5, 6, 'a'])

_list = [1, 2, 3, 4, 5, 'a']


def elementTypeOfList(_objectList):

    _outputFunction = {}

    _outputFunction['function'] = 'elementTypeOfList'

    for _index in range(0, len(_objectList)):

        _outputFunction['index'+' '+str(_index)] = _index

        _outputFunction['element'+' '+str(_index)] = _objectList[_index]

        _outputFunction['type of'+' '+str(_index)] = type(_objectList[_index])

    pprint.pprint(_outputFunction)

    print("\n")

    return _outputFunction


def elementTypeOfArray(_objectArray):

    _outputFunction = {}

    _outputFunction['function'] = 'elementTypeOfArray'

    for _index in range(0, len(_objectArray)):

        _outputFunction['index'+' '+str(_index)] = _index

        _outputFunction['element'+' '+str(_index)] = _objectArray[_index]

        _outputFunction['type of'+' '+str(_index)] = type(_objectArray[_index])

    pprint.pprint(_outputFunction)

    print("\n")

    return _outputFunction


elementTypeOfList(_list)

elementTypeOfArray(_array)


def applyToList(_objectList: list, _function):

    _outputFunction = {}

    _outputFunction['function'] = 'applyToList'

    _mainList = copy.deepcopy(_objectList)

    _outputFunction['main list'] = _mainList

    _outputFunction['new list'] = _function(_objectList)

    print("\n")

    pprint.pprint(_outputFunction)

    return _outputFunction


def upperList(_objectList):

    _outputFunction = [_element.upper() for _element in _objectList]

    return _outputFunction

def typeToString(_objectList):
    
    _outputFunction = [str(_element) for _element in _objectList]

    return _outputFunction

_stringList = applyToList(_list, typeToString)

print(_stringList)

elementTypeOfList(_stringList['new list'])

