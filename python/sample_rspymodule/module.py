from sample_rspymodule._lowlevel import hello


def pymodule_f(arg: str):
    print("Python module called with arg:", arg)
    result = hello()
    print("End of Python module: ", result)


def miss_pymodule_f(arg: str):
    print("Python module called with arg:", arg)
    hello()
    print("End of Python module: None")
