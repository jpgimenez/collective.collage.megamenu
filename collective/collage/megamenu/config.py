HAS_HIDDENCONTENT = False
try:
    from collective.hiddencontent.browser.interfaces import IHiddenContentLayer
    HAS_HIDDENCONTENT = True
except ImportError:
    pass
    

