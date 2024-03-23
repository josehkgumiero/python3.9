# python ./data_structure_algorithms/list_functions.py

import list as _list

import pprint

import copy


def toDictionary(_objectList):

    _outputFunction = {}

    _outputFunction['list'] = _objectList

    print(_outputFunction)

    print("\n")


def forEach(_object):
    for _element in _object:
        print(_element)


def accessList(_objectList):

    _outputFunction = {}

    _outputFunction['function'] = 'accessList'

    _outputFunction['list'] = _objectList

    _outputFunction['range'] = int(len(_objectList))

    for _index in range(int(len(_objectList))):

        _outputFunction['index'+' '+str(_index)] = _objectList[_index]

    pprint.pprint(_outputFunction)

    print("\n")

    return _outputFunction


def insertList(_objectList: list, _elementPosition, _element):

    _outputFunction = {}

    _oldList = copy.deepcopy(_objectList)

    _newList = copy.deepcopy(_objectList)

    _outputFunction['old list'] = _oldList

    _newList.insert(_elementPosition, _element)

    _outputFunction['new list'] = _newList

    pprint.pprint(_outputFunction)

    return _outputFunction


def insertToList(_objectList: list, _elementPosition, _element):

    _outputFunction = {}

    _outputFunction['function'] = 'insertToList'

    _oldList = copy.deepcopy(_objectList)

    _newList = copy.deepcopy(_objectList)

    _outputFunction['old list'] = _oldList

    _newList.insert(_elementPosition, _element)

    _outputFunction['new list'] = _newList

    print("\n")

    pprint.pprint(_outputFunction)

    return _outputFunction


def appendTotList(_objectList: list, _element):

    _outputFunction = {}
    
    _outputFunction['function'] = 'appendTotList'

    _oldList = copy.deepcopy(_objectList)
    
    _newList = copy.deepcopy(_objectList)

    _outputFunction['old list'] = _oldList

    _newList.append(_element)

    _outputFunction['new list'] = _newList

    print("\n")

    pprint.pprint(_outputFunction)

    return _outputFunction


def extendList(_objectListA: list, _objectListB: list):

    _outputFunction = {}

    _outputFunction['function'] = 'extendList'

    _mainList = copy.deepcopy(_objectListA)

    _extendedList = copy.deepcopy(_objectListA)

    _otherList = copy.deepcopy(_objectListB)

    _outputFunction['main list'] = _mainList

    _outputFunction['other list'] = _otherList

    _extendedList.extend(_otherList)

    _outputFunction['extended list'] = _extendedList

    print("\n")

    pprint.pprint(_outputFunction)

    return _outputFunction


def removeFromIndex(_objectList: list, _elementPosition):

    _outputFunction = {}

    _outputFunction['function'] = 'removeFromIndex'

    _mainList = copy.deepcopy(_objectList)

    _newList = copy.deepcopy(_objectList)

    _outputFunction['main list'] = _mainList

    _newList.pop(_elementPosition)

    _outputFunction['new list'] = _newList

    print("\n")

    pprint.pprint(_outputFunction)

    return _outputFunction


def deleteSlice(_objectList: list, _startPosition, _lastPosition, _jumpIndexPosition=1):

    _outputFunction = {}

    _outputFunction['function'] = 'deleteSlice'

    _mainList = copy.deepcopy(_objectList)

    _newList = copy.deepcopy(_objectList)

    _outputFunction['main list'] = _mainList

    del _newList[_startPosition:_lastPosition:_jumpIndexPosition]

    _outputFunction['new list'] = _newList

    print("\n")

    pprint.pprint(_outputFunction)

    return _outputFunction


def removeElement(_objectList: list, _element):

    _outputFunction = {}

    _outputFunction['function'] = 'removeElement'

    _mainList = copy.deepcopy(_objectList)

    _newList = copy.deepcopy(_objectList)

    _outputFunction['main list'] = _mainList

    _newList.remove(_element)

    _outputFunction['new list'] = _newList

    print("\n")

    pprint.pprint(_outputFunction)

    return _outputFunction


def inList(_objectList: list, _element):

    _outputFunction = {}

    _outputFunction['function'] = 'inList'

    _mainList = copy.deepcopy(_objectList)

    _outputFunction['main list'] = _mainList

    _outputFunction['element'] = _element

    _in = False

    if _element in _objectList:

        _in = True

    _outputFunction['in'] = _in

    print("\n")

    pprint.pprint(_outputFunction)

    return _outputFunction


def linearSearch(_objectList: list, _element):

    _outputFunction = {}

    _outputFunction['function'] = 'linearSearch'

    _mainList = copy.deepcopy(_objectList)

    _outputFunction['main list'] = _mainList

    _outputFunction['element'] = _element

    for _index, _value in enumerate(_objectList):
        if _value == _element:
            _outputFunction['index'] = _index

    print("\n")

    pprint.pprint(_outputFunction)

    return _outputFunction


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


def splitStringToList(_objectString: str, _delimiter):

    _outputFunction = {}

    _outputFunction['function'] = 'splitStringToList'

    _mainString = copy.deepcopy(_objectString)

    _splitedString = copy.deepcopy(_objectString)

    _outputFunction['main string'] = _mainString

    _splitedString = _splitedString.split(_delimiter)

    _outputFunction['splited string'] = _splitedString

    print("\n")

    pprint.pprint(_outputFunction)

    return _outputFunction


def joinStringToList(_objectList: list, _delimiter: str):

    _outputFunction = {}

    _outputFunction['function'] = 'joinStringToList'

    _mainList = copy.deepcopy(_objectList)

    _outputFunction['main list'] = _mainList

    _outputFunction['main string'] =  _delimiter.join(_mainList)

    print("\n")

    pprint.pprint(_outputFunction)

    return _outputFunction


if __name__ == "__main__":

    _list.initializeLists()

    accessList(_list._integerList)
    
    accessList(_list._stringList)
    
    accessList(_list._mixedList)
    
    accessList(_list._nestedList)
    
    accessList(_list._emptyList)
    
    insertToList(_list._integerList, 1, [100, 200, 300])
    
    appendTotList(_list._integerList, 100)
    
    extendList(_list._integerList, _list._stringList)
    
    removeFromIndex(_list._integerList, 0)
    
    deleteSlice(_list._integerList, 2, 4)
    
    removeElement(_list._integerList, 1)
    
    inList(_list._integerList, 1)
    
    linearSearch(_list._integerList, 1)
    
    applyToList(_list._stringList, upperList)

    splitStringToList(_list._stringHello, 'o')

    joinStringToList(splitStringToList(_list._stringHello, 'o')['splited string'], 'o')
