from OEIS import G000017 as func
LOW = 0; HIGH = 20; GENERATOR = True

if GENERATOR: func = func()
for i in range(LOW, HIGH):
    print(str(next(func) if GENERATOR else func(i)) + ", ", end='')
print("End")