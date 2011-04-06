from zope.interface import Interface, Attribute
from zope.schema import Bool, Choice
from collective.collage.megamenu import message_factory as _

class IDisplayingMegamenuLayer(Interface):
    """ 
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
                              
class ICookedSettingsView(Interface):
    """ A browser view with some processing of control panel settings
    """
    
    def resolve_folder(UID):
        """ Given a UID, get the folder via catalog
        """
    
    menufolder = Attribute("""Folder that is used to display megamenu""")
    enabled = Attribute("""Should display megamenu? Folder is megamenu-enabled?""")
    ajax = Attribute("""Load drop-down submenues via AJAX""")
