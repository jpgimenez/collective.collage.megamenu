from Acquisition import aq_inner
from plone.app.layout.viewlets import common
from zope.component import getMultiAdapter
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class MegamenuViewlet(common.ViewletBase):
    """ Viewlet to display megamenu
    """
    
    def update(self):
        context = aq_inner(self.context)
        request = self.request
        settings = getMultiAdapter((context, request), name="megamenu-settings")
        self.menufolder = settings.menufolder
        self.has_megamenu = not self.menufolder is None
        
    index = ViewPageTemplateFile('templates/viewlet.pt')
