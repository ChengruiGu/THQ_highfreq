__config__ = {
    "url": None,

}


def load_mod():
    from .mod import thqDataMod
    return thqDataMod()
