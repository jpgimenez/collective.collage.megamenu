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
        # If testing a megamenu, use the requested folder instead of the one
        # specified in controlpanel
        test_folder = request.form.get('megamenu-test')
        settings = getMultiAdapter((context, request), name="megamenu-settings")
        if test_folder:
            self.menufolder = settings.resolve_folder(test_folder)
            self.testing = settings.menufolder.UID() != test_folder
        else:
            self.menufolder = settings.menufolder
            self.testing = False
            
        if not IMegamenuEnabled in providedBy(self.menufolder):
            self.menufolder = None
        self.has_megamenu = not self.menufolder is None
        
    index = ViewPageTemplateFile('templates/viewlet.pt')
