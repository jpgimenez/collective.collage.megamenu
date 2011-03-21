from zope.interface import Interface
from zope.schema import TextLine
from collective.collage.megamenu import message_factory as _

class IDisplayingMegamenuLayer(Interface):
    """ A
    """


class IMegamenuLayer(Interface):
    """ A layer specific to this product.
        Is registered using browserlayer.xml
    """

class IMegamenuEnabled(Interface):
    """ A marker interface to enable a folder
        as a megamenu
    """

class IMegamenuCapable(Interface):
    """ A marker interface applied to all folders
    """

class IMegamenuSettings(Interface):
    """ An interface to support configlet settings
    """

    megamenu_folder = TextLine(title=_(u"Megamenu folder UID"),
                               required=False)
