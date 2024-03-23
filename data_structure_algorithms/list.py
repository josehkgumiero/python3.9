def initializeLists():

    global _integerList
    global _stringList
    global _mixedList
    global _nestedList
    global _emptyList
    
    global _stringHello

    _integerList = [1, 2, 3, 4]
    _stringList = ['Milk', 'Cheese', 'Butter']
    _mixedList = [1, 2.3, 'spam']
    _nestedList = [1, 2, 3, 4, 5, [1.4, 1.6], ['test']]
    _emptyList = []

    _stringHello = 'Hello, World'


def toDictionary():

    return {
        'integerList': _integerList,
        'string': _stringList,
        'mixedList': _mixedList,
        'nestedList': _nestedList,
        'emptyList': _emptyList,
        '_stringHello': _stringHello
    }
