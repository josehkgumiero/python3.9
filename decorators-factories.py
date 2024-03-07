def timed(fn):
    
    from time import perf_counter

    def inner(*args, **kwargs):

        start = perf_counter()

        result = fn(*args, **kwargs)

        end = perf_counter()

        elapsed = end - start

        print(
            """
            Run time: {0:.6f}s
            """ \
            .format(elapsed)
        )

        return result
    
    return inner

def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n-2) + calc_fib_recurse(n-1)

def fib(n):
    return calc_fib_recurse(n)

fib = timed(fib)

print(
    fib(30)
)

def timed(fn, reps):

    from time import perf_counter

    def inner(*args, **kwargs):
        
        total_elapsed = 0
        
        for i in range(10):

            start = perf_counter()

            result = fn(*args, **kwargs)

            end = perf_counter()

            total_elapsed += (end - start)

        avg_run_time = total_elapsed / 10

        print(
            """
            Avg Run tme: {0:.6f}s
            """ \
            .format(avg_run_time)
        )

        return result
    
    return inner

def fib(n):
    return calc_fib_recurse(n)

fib = timed(fib, 5)

print(
    fib(28)
)

def dec(fn):
    print("Running dec")

    def inner(*args, **kwargs):
        print("Running inner")
        return fn(*args, **kwargs)
    
    return inner

@dec
def fn():
    print("Running fn")

def fn():
    print("Running fn")

fn = dec(fn)

print(fn)

print(
    fn()
)

def dec_factory():
    print("Running dec_factory")

    def dec(fn):
        print("Running dec")

        def inner(*args, **kwargs):
            print("RUnning inner")
            return fn(*args, **kwargs)
        
        return inner
    
    return dec

dec = dec_factory()

print(
    dec
)

@dec
def fn():
    print("Running fn")

print(
    fn
)

@dec_factory()
def fn():
    print("Running fn")

fn = dec_factory()(fn)

print(fn)

def dec_factory(a, b):
    print("Running dec_faactory")

    def dec(fn):
        print("Running dec")

        def inner(*args, **kwargs):
            print("Running inner")
            print("a = {0}, b= {1}".format(a, b))
            return fn(*args, **kwargs)
        
        return inner
    
    return dec

dec = dec_factory(10, 20)

print(dec)

@dec
def fn():
    print("Running fn")

print(
    fn()
)

@dec_factory(100, 200)
def fn():
    print("Running fn")

print(
    fn
)

def fn():
    print("Running fn")

fn = dec_factory(150, 250)(fn)

print(
    fn()
)

def dec_factory(reps):
    def timed(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (end - start)
            
            avg_run_time = total_elapsed / reps

            print(
                """
                Avg Run Time: {0:.6f}s ({1} reps) \
                """ \
                .format(avg_run_time, reps)
            )

            return result
        
        return inner

@dec_factory(5)
def fib(n):
    return calc_fib_recurse(n)

print(
    fib(28)
)

@timed(15)
def fib(n):
    return calc_fib_recurse(n)

print(
    fib(28)
)