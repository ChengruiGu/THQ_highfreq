__config__ = {
    "url": None,

}


def load_mod():
    from .mod import HelloWorldMod
    return HelloWorldMod()