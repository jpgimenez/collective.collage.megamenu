from zope.interface import Interface
from zope.schema import Bool, Choice
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

    enabled = Bool(title=_(u"Display megamenu"))

    megamenu_folder = Choice(title=_(u"Megamenu folder"), 
                             vocabulary='collective.collage.megamenues',
                             required=False)

    deferred_rendering = Bool(title=_(u"Load dropdown menu via AJAX"),
                              description=_(u"If selected, dropdown options will not be included in original HTML but loaded via AJAX. These options won't be available for search engines."))
