import ctypes

def ref_count(address):
    return \
        ctypes.c_long.from_address(address).value

def object_by_id(object_id):
    for \
        obj in gc.get_objects():
            if \
                id(obj) == object_id:
                    return \
                        '''Object exists'''
    return \
        '''Not found'''

import gc

gc.disable()

class A:
      def __init__(self):
            self.b = B(self)
            print(
                    '''
                    A: self: {0}, b: {1}
                    ''' \
                    .format(
                          hex(
                                id(
                                      self
                                )
                          ),
                          hex(
                                id(
                                      self.b
                                )
                          )
                    )
            )

class B:
      def __init__(self, a):
            self.a = a
            print(
                    '''
                    B: self: {0}, a: {1}
                    ''' \
                    .format(
                          hex(
                                id(
                                      self
                                )
                          ),
                          hex(
                                id(
                                      self.a
                                )
                          )
                    )
            )

a = A()

print(
      hex(
            id(
                  a
            )
      )
)

print(
      hex(
            id(
                  a.b
            )
      )
)

print(
      hex(
            id(
                  a.b.a
            )
      )
)

print(
    ref_count(
        id(
              a
        )
    )    
)

print(
    ref_count(
        id(
              a.b
        )
    )    
)

print(
      object_by_id(
            id(
                  a
            )
      )
)

print(
      object_by_id(
            id(
                  a.b
            )
      )
)

gc.collect()


print(
      object_by_id(
            id(
                  a
            )
      )
)

print(
      object_by_id(
            id(
                  a.b
            )
      )
)

print(
    ref_count(
        id(
              a
        )
    )    
)

print(
    ref_count(
        id(
              a.b
        )
    )    
)

