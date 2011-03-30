from Acquisition import aq_inner
from plone.app.layout.viewlets import common
from zope.component import getMultiAdapter
from zope.interface import providedBy
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.collage.megamenu.interfaces import IMegamenuEnabled

class MegamenuViewlet(common.ViewletBase):
    """ Viewlet to display megamenu
    """
    
    def update(self):
        context = aq_inner(self.context)
        request = self.request
        settings = getMultiAdapter((context, request), name="megamenu-settings")
        self.menufolder = settings.menufolder
        if not IMegamenuEnabled in providedBy(self.menufolder):
            self.menufolder = None
        self.has_megamenu = not self.menufolder is None
        
    index = ViewPageTemplateFile('templates/viewlet.pt')
