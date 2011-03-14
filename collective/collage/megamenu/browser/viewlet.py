from Acquisition import aq_inner
from plone.app.layout.viewlets import common
#from zope.component import queryUtility
#from plone.registry.interfaces import IRegistry
from zope.component import getMultiAdapter

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class MegamenuViewlet(common.ViewletBase):
    """ Viewlet to display megamenu
    """
    
    def update(self):
        context = aq_inner(self.context)
        request = self.request
        # TODO: get mega menu folder
        portal_state = getMultiAdapter((context, request), name="plone_portal_state")
        portal = portal_state.portal()
        self.has_megamenu = hasattr(portal, 'menu')
        if self.has_megamenu:
            self.menufolder = getattr(portal, 'menu')
        else:
            self.menufolder = None
                
    index = ViewPageTemplateFile('templates/viewlet.pt')
