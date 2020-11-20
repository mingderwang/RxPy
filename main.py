import rx
from rx import of, operators as ops


def length_less_than_5():
    return rx.pipe(
        ops.map(lambda s: len(s)),
        ops.filter(lambda i: i >= 5),
    )


of("Alpha", "Beta", "Gamma", "Delta",
   "Epsilon").pipe(length_less_than_5()).subscribe(
       lambda value: print("Received {0}".format(value)))
